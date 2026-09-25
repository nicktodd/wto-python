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
    # TODO STEP 10: if not offline, request the indicator from the World Bank API
    # (Module 05): URL, params with per_page 1000, timeout, raise_for_status(),
    # check the payload has data; return payload[1]. On
    # requests.RequestException or ValueError log a warning and fall through.
    # Finally load and return the records from config.CACHE / cache_file.
    raise NotImplementedError


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
