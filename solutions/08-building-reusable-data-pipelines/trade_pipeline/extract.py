"""Extract step: read raw files and call the World Bank API (with cache fallback)."""
import json
import logging

import pandas as pd
import requests

from . import config

log = logging.getLogger(__name__)


def read_raw_trade(path=config.RAW_TRADE_FILE):
    df = pd.read_csv(path, dtype=str)
    log.info("Read %d raw trade rows from %s", len(df), path.name)
    return df


def read_countries(path=config.COUNTRIES_FILE):
    df = pd.read_excel(path, sheet_name="countries")
    log.info("Read %d countries", len(df))
    return df


def fetch_wb_indicator(code, iso3_codes, start, end, cache_file, offline=False):
    """Return World Bank records for one indicator, falling back to the cache."""
    if not offline:
        url = f"{config.WB_BASE}/country/{';'.join(iso3_codes)}/indicator/{code}"
        params = {"format": "json", "date": f"{start}:{end}", "per_page": 1000}
        try:
            resp = requests.get(url, params=params, timeout=config.TIMEOUT_SECONDS)
            resp.raise_for_status()
            payload = resp.json()
            if len(payload) < 2 or not payload[1]:
                raise ValueError(f"API returned no data: {payload[0]}")
            log.info("Fetched %d records for %s from the API", len(payload[1]), code)
            return payload[1]
        except (requests.RequestException, ValueError) as e:
            log.warning("API request for %s failed (%s); using cache", code, e)
    records = json.loads((config.CACHE / cache_file).read_text(encoding="utf-8"))[1]
    log.info("Loaded %d cached records for %s", len(records), code)
    return records


def extract_wb(iso3_codes, start, end, offline=False):
    """Return one DataFrame with a column per configured indicator."""
    frames = []
    for column, (code, cache_file) in config.WB_INDICATORS.items():
        records = fetch_wb_indicator(code, iso3_codes, start, end, cache_file, offline)
        frames.append(pd.DataFrame({
            "iso3": [r["countryiso3code"] for r in records],
            "year": [int(r["date"]) for r in records],
            column: [r["value"] for r in records],
        }))
    wb = frames[0]
    for f in frames[1:]:
        wb = wb.merge(f, on=["iso3", "year"], how="outer")
    return wb[wb["year"].between(start, end)]
