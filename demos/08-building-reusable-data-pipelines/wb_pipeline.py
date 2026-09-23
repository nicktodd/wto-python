"""World Bank exports pipeline (demo).

Extracts exports of goods and services (% of GDP)
from the World Bank API, cleans it and writes a
reporting-ready CSV.

Usage:
    python wb_pipeline.py --start 2015 --end 2023
"""
import argparse
import json
import logging
from pathlib import Path

import pandas as pd
import requests

# ---- configuration --------------------------
BASE = "https://api.worldbank.org/v2"
INDICATOR = "NE.EXP.GNFS.ZS"
COUNTRIES = ["KEN", "NGA", "ZAF", "BRA", "IND"]
HERE = Path(__file__).parent
CACHE = HERE / "../../data/cache"
OUT = HERE / "output"

log = logging.getLogger("wb_pipeline")


def setup_logging(level="INFO"):
    OUT.mkdir(exist_ok=True)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s "
               "%(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(OUT / "run.log"),
        ],
    )


def extract(start, end):
    codes = ";".join(COUNTRIES)
    url = f"{BASE}/country/{codes}/indicator/"
    params = {"format": "json", "per_page": 1000,
              "date": f"{start}:{end}"}
    try:
        resp = requests.get(url + INDICATOR,
                            params, timeout=30)
        resp.raise_for_status()
        records = resp.json()[1]
        log.info("Extracted %d records from API",
                 len(records))
    except (requests.RequestException,
            IndexError, TypeError) as e:
        log.warning("API failed: %s; using cache",
                    e)
        path = CACHE / "wb_exports_pct_gdp.json"
        text = path.read_text(encoding="utf-8")
        records = json.loads(text)[1]
    return records


def transform(records, start, end):
    rows = [{"iso3": r["countryiso3code"],
             "country": r["country"]["value"],
             "year": int(r["date"]),
             "value": r["value"]}
            for r in records]
    df = pd.DataFrame(rows)
    df = df[df["iso3"].isin(COUNTRIES)
            & df["year"].between(start, end)]
    missing = df["value"].isna().sum()
    if missing:
        log.warning("%d missing values", missing)
    df["value"] = df["value"].round(1)
    df = df.rename(
        columns={"value": "exports_pct_gdp"})
    return df.sort_values(["iso3", "year"])


def validate(df):
    assert not df.empty, "no data"
    assert df["iso3"].nunique() == len(COUNTRIES)
    dups = df.duplicated(["iso3", "year"])
    assert not dups.any(), "duplicate keys"
    log.info("Validated %d rows", len(df))


def load(df):
    path = OUT / "exports_pct_gdp.csv"
    df.to_csv(path, index=False)
    log.info("Wrote %s", path)
    return path


def main():
    parser = argparse.ArgumentParser(
        description="World Bank exports pipeline")
    parser.add_argument("--start", type=int,
                        default=2015)
    parser.add_argument("--end", type=int,
                        default=2023)
    args = parser.parse_args()

    setup_logging()
    log.info("Run started: %s-%s",
             args.start, args.end)
    records = extract(args.start, args.end)
    df = transform(records, args.start, args.end)
    validate(df)
    load(df)
    log.info("Run finished")


if __name__ == "__main__":
    main()
