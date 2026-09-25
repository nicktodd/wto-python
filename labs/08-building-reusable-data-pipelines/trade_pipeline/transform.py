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


def standardise_text(df):
    """Lower-case the column names, strip spaces from every value, map reporter variants."""
    # TODO STEP 2: copy df; lower-case and strip the column names;
    # strip every text column (df[col].str.strip()); map df["reporter"]
    # with config.NAME_MAP. Return df.  (Module 07, Part B)
    raise NotImplementedError


def convert_values(df):
    """Make value numeric and in USD millions; make negative values positive."""
    # TODO STEP 3: copy df; df["value"] = to_number(df["value"]);
    # divide USD thousands rows by 1000 and set their unit to USD millions;
    # make negative values positive with .abs(). Log each step with a count.
    # (Module 07, Part C)
    raise NotImplementedError


def add_year(df):
    """Add an int year column parsed from period; drop rows that cannot be parsed."""
    # TODO STEP 4: copy df; df["year"] = df["period"].map(parse_year);
    # drop rows where year is missing (log a warning if any); convert year to int.
    raise NotImplementedError


def remove_duplicates(df):
    """Keep one row per (reporter, partner, year), preferring rows that have a value."""
    # TODO STEP 5: sort by value with na_position="last", then
    # drop_duplicates(["reporter", "partner", "year"], keep="first").
    # Log how many rows were removed.
    raise NotImplementedError


def clean_trade(raw):
    """Run every cleaning step in order and return the analysis-ready table."""
    df = standardise_text(raw)
    df = convert_values(df)
    df = add_year(df)
    df = remove_duplicates(df)
    df["value_missing"] = df["value"].isna()
    log.info("%d rows have missing values (flagged)", df["value_missing"].sum())
    return df.drop(columns=["period"]).rename(columns={"value": "exports_usd_m"})


def add_reference_data(df, countries):
    # TODO STEP 6: left-merge countries[["iso3", "country_name", "region", "income_group"]]
    # on reporter / country_name with validate="many_to_one"; drop country_name.
    # Raise ValueError listing any reporters with no iso3.
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
    # TODO STEP 7: return a list of problems (empty = OK). If a required column is
    # missing return ["missing columns: ..."]. Otherwise check: "negative values",
    # "unmatched reporters" (iso3 missing), "duplicate keys" (iso3, partner, year),
    # "years out of range" (config.START_YEAR..END_YEAR), "mixed units".
    raise NotImplementedError


def summarise(df):
    """Reporting table: World exports by region and year, USD billions."""
    # TODO STEP 8: keep partner == "World"; pivot_table with index region, columns year,
    # values exports_usd_m, aggfunc sum; divide by 1000 and round to 1 dp.
    raise NotImplementedError
