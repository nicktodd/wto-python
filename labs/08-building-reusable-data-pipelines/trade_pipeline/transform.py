"""Transform step: clean the raw trade data, merge reference and World Bank data."""
import logging

import pandas as pd

from . import config

log = logging.getLogger(__name__)


def parse_year(period):
    """Return the year from a period string in any configured format, or None."""
    for fmt in config.PERIOD_FORMATS:
        try:
            return pd.to_datetime(str(period).strip(), format=fmt).year
        except ValueError:
            continue
    return None


def to_number(series):
    """Convert text such as '1,234.5' or 'n/a' to floats (invalid -> NaN)."""
    text = series.astype(str).str.replace(",", "", regex=False).str.strip()
    return pd.to_numeric(text, errors="coerce")


def clean_trade(raw):
    # TODO: Apply the Module 07 cleaning steps, logging each one with a row count:
    #   1. lower-case/strip column names; strip text values
    #   2. map reporter names with config.NAME_MAP
    #   3. convert value with to_number(); convert USD thousands to USD millions
    #   4. make negative values positive (or set to missing) and log it
    #   5. derive an int year column with parse_year(); drop unparseable rows
    #   6. drop duplicate (reporter, partner, year) keys, keeping non-missing values
    #   7. add a value_missing flag
    # Return the frame without 'period', with 'value' renamed to 'exports_usd_m'.
    raise NotImplementedError


def add_reference_data(df, countries):
    # TODO: Left-merge iso3, region and income_group from countries on reporter/country_name
    # with validate='many_to_one'. Raise ValueError listing any unmatched reporters.
    raise NotImplementedError


def add_indicators(df, wb):
    merged = df.merge(wb, on=["iso3", "year"], how="left", validate="many_to_one")
    world = merged["partner"] == "World"
    merged.loc[world, "exports_pct_gdp_calc"] = (
        merged.loc[world, "exports_usd_m"] * 1e6 / merged.loc[world, "gdp_usd"] * 100
    ).round(1)
    return merged


def validate(df):
    """Return a list of problems; an empty list means the data is ready."""
    # TODO: Return a list of problems (empty list = OK). Check: required columns exist,
    # no negative exports_usd_m, no missing iso3, no duplicate (iso3, partner, year),
    # years within config.START_YEAR..config.END_YEAR, unit is always 'USD millions'.
    raise NotImplementedError


def summarise(df):
    """Reporting table: World exports by region and year, USD billions."""
    # TODO: Return World exports by region (rows) and year (columns) in USD billions, 1 dp.
    raise NotImplementedError
