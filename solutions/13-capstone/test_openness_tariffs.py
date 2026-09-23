"""Tests for the capstone worked example. Run: pytest solutions/13-capstone -v"""
import json

import pandas as pd
import pytest

import openness_tariffs as ot


@pytest.fixture
def countries():
    return pd.DataFrame({"iso3": ["AAA", "BBB"], "country_name": ["Aland", "Bland"],
                         "income_group": ["High income", "Low income"]})


@pytest.fixture
def frames():
    exports = pd.DataFrame({"iso3": ["AAA", "AAA", "BBB", "BBB"],
                            "year": [2015, 2023, 2015, 2023],
                            "exports_pct_gdp": [20.0, 30.0, 50.0, 40.0]})
    tariffs = pd.DataFrame({"iso3": ["AAA", "AAA", "BBB", "BBB"],
                            "year": [2015, 2023, 2015, 2023],
                            "tariff_pct": [2.0, 2.0, 10.0, None]})
    return [exports, tariffs]


def test_records_to_frame_handles_missing_values():
    recs = [{"countryiso3code": "KEN", "date": "2023", "value": None},
            {"countryiso3code": "KEN", "date": "2022", "value": 12.5}]
    df = ot.records_to_frame(recs, "x")
    assert df["year"].dtype.kind == "i"
    assert df["x"].isna().sum() == 1


def test_build_panel_merges_and_validates(frames, countries):
    panel = ot.build_panel(frames, countries)
    assert len(panel) == 4
    assert ot.validate(panel, 2) == []


def test_validate_detects_unknown_economy(frames, countries):
    panel = ot.build_panel(frames, countries[countries["iso3"] == "AAA"])
    assert "economies missing from reference data" in ot.validate(panel, 2)


def test_openness_change(frames, countries):
    change = ot.openness_change(ot.build_panel(frames, countries))
    assert change.loc[("Aland", "High income"), "change_pts"] == 10.0
    assert change.loc[("Bland", "Low income"), "change_pts"] == -10.0


def test_correlation_uses_country_averages(frames, countries):
    corr, n = ot.tariff_openness_correlation(ot.build_panel(frames, countries))
    assert n == 2
    assert corr == pytest.approx(1.0)     # two points are always perfectly correlated


def test_cache_files_have_expected_shape():
    for _, cache_file in ot.INDICATORS.values():
        meta, records = json.loads((ot.CACHE / cache_file).read_text(encoding="utf-8"))
        assert meta["total"] == len(records) == 126      # 14 economies x 9 years
