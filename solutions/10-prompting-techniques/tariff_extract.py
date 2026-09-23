"""Extract the World Bank applied tariff rate for the course economies.

Indicator TM.TAX.MRCH.SM.AR.ZS: tariff rate, applied, simple mean, all products (%).
Produces output/tariffs_wb.csv with columns iso3, country, year, tariff_pct.

Usage (from the repository root):
    python solutions/10-prompting-techniques/tariff_extract.py
    python solutions/10-prompting-techniques/tariff_extract.py --offline

Assumptions (listed by the assistant, confirmed by the analyst):
- "Applied, simple mean" is an unweighted average across tariff lines; it is not
  the trade-weighted rate (TM.TAX.MRCH.WM.AR.ZS).
- Missing years are genuinely unpublished and are kept as missing, not filled.
- The World Bank returns every record in one page when per_page >= total.
"""
import argparse
import json
import logging
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
CACHE_FILE = ROOT / "data" / "cache" / "wb_tariff_applied_mean.json"
OUT_FILE = Path(__file__).resolve().parent / "output" / "tariffs_wb.csv"

BASE = "https://api.worldbank.org/v2"
INDICATOR = "TM.TAX.MRCH.SM.AR.ZS"
COUNTRIES = ["AUS", "BRA", "CAN", "CHN", "DEU", "IND", "JPN",
             "KEN", "MEX", "NGA", "GBR", "USA", "VNM", "ZAF"]
START, END = 2015, 2023

log = logging.getLogger("tariff_extract")


def fetch_records(offline=False):
    """Return raw World Bank records, from the API or (on failure / offline) the cache."""
    if not offline:
        url = f"{BASE}/country/{';'.join(COUNTRIES)}/indicator/{INDICATOR}"
        params = {"format": "json", "date": f"{START}:{END}", "per_page": 1000}
        try:
            resp = requests.get(url, params=params, timeout=30)
            resp.raise_for_status()
            payload = resp.json()
            # The API reports some errors with HTTP 200 and a message instead of data.
            if len(payload) < 2 or not payload[1]:
                raise ValueError(f"API returned no data: {payload[0]}")
            log.info("Fetched %d records from the World Bank API", len(payload[1]))
            return payload[1]
        except (requests.RequestException, ValueError) as e:
            log.warning("API unavailable (%s); falling back to cached data", e)
    records = json.loads(CACHE_FILE.read_text(encoding="utf-8"))[1]
    log.info("Loaded %d records from %s", len(records), CACHE_FILE.name)
    return records


def to_frame(records):
    """Convert records to a tidy DataFrame; missing values stay as NaN."""
    df = pd.DataFrame({
        "iso3": [r["countryiso3code"] for r in records],
        "country": [r["country"]["value"] for r in records],
        "year": [int(r["date"]) for r in records],
        "tariff_pct": [r["value"] for r in records],
    })
    df["tariff_pct"] = pd.to_numeric(df["tariff_pct"])
    return df.sort_values(["iso3", "year"]).reset_index(drop=True)


def check(df):
    """Fail loudly if the result does not have the expected shape."""
    expected = len(COUNTRIES) * (END - START + 1)
    if len(df) != expected:
        raise ValueError(f"Expected {expected} rows, got {len(df)}")
    if df.duplicated(["iso3", "year"]).any():
        raise ValueError("Duplicate country-year rows")
    log.info("%d rows; %d missing tariff values", len(df), df["tariff_pct"].isna().sum())


def save(df, path=OUT_FILE):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    log.info("Wrote %s", path)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--offline", action="store_true", help="use the cached response only")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    df = to_frame(fetch_records(args.offline))
    check(df)
    save(df)


if __name__ == "__main__":
    main()
