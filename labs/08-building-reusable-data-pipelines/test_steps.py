"""Step-by-step checks for the trade pipeline.

Run ONE step at a time from this folder (the one containing trade_pipeline/):
    pytest test_steps.py -k step01 -v
    pytest test_steps.py -k step02 -v
    ...
Run them all at the end:
    pytest test_steps.py -v
"""
import logging
from pathlib import Path

import pandas as pd
import pytest

from trade_pipeline import config, extract, load, run_pipeline, transform


@pytest.fixture
def raw():
    return pd.DataFrame({
        "Reporter": [" USA", "Kenya", "Kenya", "Vietnam "],
        "Partner":  ["World", "World", "World", "World"],
        "Period":   ["2021-12-31", "Dec 2021", "2021", "31/12/2022"],
        "Flow":     ["Exports"] * 4,
        "Value":    ["1,500.5", "n/a", "7400", "-20"],
        "Unit":     ["USD millions", "USD millions", "USD thousands", "USD millions"],
    })


# ---- Step 1: command line and logging (run_pipeline.py) -------------------
def test_step01_parse_args_defaults():
    args = run_pipeline.parse_args([])
    assert args.offline is False and args.verbose is False
    assert Path(args.out) == config.DEFAULT_OUT


def test_step01_parse_args_flags(tmp_path):
    args = run_pipeline.parse_args(["--offline", "--verbose", "--out", str(tmp_path)])
    assert args.offline and args.verbose and Path(args.out) == tmp_path


def test_step01_setup_logging_writes_file(tmp_path):
    root = logging.getLogger()
    old = root.handlers[:]
    root.handlers.clear()
    try:
        run_pipeline.setup_logging(tmp_path)
        logging.getLogger("trade_pipeline").info("hello")
        for h in root.handlers:
            h.flush()
        assert "hello" in (tmp_path / "pipeline.log").read_text()
    finally:
        for h in root.handlers:
            h.close()
        root.handlers[:] = old


# ---- Step 2: standardise_text (transform.py) ------------------------------
def test_step02_standardise_text(raw):
    df = transform.standardise_text(raw)
    assert list(df.columns) == ["reporter", "partner", "period", "flow", "value", "unit"]
    assert list(df["reporter"]) == ["United States", "Kenya", "Kenya", "Viet Nam"]


# ---- Step 3: convert_values -----------------------------------------------
def test_step03_convert_values(raw):
    df = transform.convert_values(transform.standardise_text(raw))
    assert df["value"].iloc[0] == 1500.5          # comma removed
    assert pd.isna(df["value"].iloc[1])           # n/a -> missing
    assert df["value"].iloc[2] == 7.4             # thousands -> millions
    assert df["value"].iloc[3] == 20.0            # negative made positive
    assert (df["unit"] == "USD millions").all()


# ---- Step 4: add_year -----------------------------------------------------
def test_step04_add_year(raw):
    df = transform.add_year(transform.standardise_text(raw))
    assert list(df["year"]) == [2021, 2021, 2021, 2022]
    assert df["year"].dtype.kind == "i"


# ---- Step 5: remove_duplicates --------------------------------------------
def test_step05_remove_duplicates_keeps_the_value(raw):
    df = transform.add_year(transform.convert_values(transform.standardise_text(raw)))
    out = transform.remove_duplicates(df)
    kenya = out[out["reporter"] == "Kenya"]
    assert len(out) == 3 and len(kenya) == 1 and kenya["value"].iloc[0] == 7.4


# ---- Step 6: add_reference_data -------------------------------------------
def test_step06_add_reference_data():
    countries = extract.read_countries()
    df = pd.DataFrame({"reporter": ["Kenya", "Viet Nam"], "partner": ["World"] * 2})
    out = transform.add_reference_data(df, countries)
    assert list(out["iso3"]) == ["KEN", "VNM"]
    assert {"region", "income_group"} <= set(out.columns)
    with pytest.raises(ValueError):
        transform.add_reference_data(pd.DataFrame({"reporter": ["Atlantis"]}), countries)


# ---- Step 7: validate ------------------------------------------------------
def good_rows():
    return pd.DataFrame({"iso3": ["KEN"], "reporter": ["Kenya"], "partner": ["World"],
                         "year": [2021], "exports_usd_m": [7.4], "unit": ["USD millions"]})


def test_step07_validate_accepts_good_data():
    assert transform.validate(good_rows()) == []


@pytest.mark.parametrize("column, value, problem", [
    ("exports_usd_m", -1.0, "negative values"),
    ("iso3", None, "unmatched reporters"),
    ("year", 1990, "years out of range"),
    ("unit", "USD thousands", "mixed units"),
])
def test_step07_validate_finds_problems(column, value, problem):
    df = good_rows()
    df[column] = [value]
    assert problem in transform.validate(df)


def test_step07_validate_finds_duplicates():
    assert "duplicate keys" in transform.validate(pd.concat([good_rows(), good_rows()]))


# ---- Step 8: summarise -----------------------------------------------------
def test_step08_summarise():
    df = pd.DataFrame({"partner": ["World", "World", "Africa"], "region": ["X", "X", "X"],
                       "year": [2021, 2021, 2021], "exports_usd_m": [1000.0, 500.0, 99.0]})
    s = transform.summarise(df)
    assert s.loc["X", 2021] == 1.5                 # World rows only, in billions


# ---- Step 9: write_outputs (load.py) --------------------------------------
def test_step09_write_outputs(tmp_path):
    df = good_rows()
    load.write_outputs(df, pd.DataFrame({"a": [1]}), tmp_path, {"source": "test"})
    assert (tmp_path / "trade_reporting.csv").exists()
    assert set(pd.ExcelFile(tmp_path / "trade_reporting.xlsx").sheet_names) == {
        "data", "exports_by_region_bn", "metadata"}
    assert '"rows": 1' in (tmp_path / "metadata.json").read_text()


# ---- Step 10: fetch_wb_indicator (extract.py) ------------------------------
def test_step10_fetch_offline_uses_cache():
    recs = extract.fetch_wb_indicator("NY.GDP.MKTP.CD", ["KEN"], 2019, 2023,
                                      "wb_gdp_usd.json", offline=True)
    assert len(recs) == 126


def test_step10_fetch_falls_back_when_api_fails(monkeypatch):
    import requests

    def broken(*args, **kwargs):
        raise requests.ConnectionError("no network")
    monkeypatch.setattr(extract.requests, "get", broken)
    recs = extract.fetch_wb_indicator("NY.GDP.MKTP.CD", ["KEN"], 2019, 2023, "wb_gdp_usd.json")
    assert len(recs) == 126
