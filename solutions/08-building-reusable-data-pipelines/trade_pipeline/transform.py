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
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    for col in df.columns:
        df[col] = df[col].str.strip()
    df["reporter"] = df["reporter"].replace(config.NAME_MAP)
    return df


def convert_values(df):
    """Make value numeric and in USD millions; make negative values positive."""
    df = df.copy()
    df["value"] = to_number(df["value"])

    thousands = df["unit"] == "USD thousands"
    df.loc[thousands, "value"] /= 1000
    df.loc[thousands, "unit"] = "USD millions"
    log.info("Converted %d rows from USD thousands", thousands.sum())

    negative = df["value"] < 0
    df.loc[negative, "value"] = df.loc[negative, "value"].abs()
    if negative.any():
        log.warning("Made %d negative values positive (sign errors)", negative.sum())
    return df


def add_year(df):
    """Add an int year column parsed from period; drop rows that cannot be parsed."""
    df = df.copy()
    df["year"] = df["period"].map(parse_year)
    unparsed = df["year"].isna().sum()
    if unparsed:
        log.warning("Dropping %d rows with unparseable periods", unparsed)
        df = df.dropna(subset=["year"])
    df["year"] = df["year"].astype(int)
    return df


def remove_duplicates(df):
    """Keep one row per (reporter, partner, year), preferring rows that have a value."""
    before = len(df)
    df = (df.sort_values("value", na_position="last")
            .drop_duplicates(["reporter", "partner", "year"], keep="first"))
    log.info("Removed %d duplicate rows", before - len(df))
    return df


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
    merged = df.merge(
        countries[["iso3", "country_name", "region", "income_group"]],
        left_on="reporter", right_on="country_name", how="left",
        validate="many_to_one",
    ).drop(columns="country_name")
    unmatched = merged.loc[merged["iso3"].isna(), "reporter"].unique()
    if len(unmatched):
        raise ValueError(f"Reporters not in reference data: {list(unmatched)}")
    return merged


def add_indicators(df, wb):
    merged = df.merge(wb, on=["iso3", "year"], how="left", validate="many_to_one")
    world = merged["partner"] == "World"
    merged.loc[world, "exports_pct_gdp_calc"] = (
        merged.loc[world, "exports_usd_m"] * 1e6 / merged.loc[world, "gdp_usd"] * 100
    ).round(1)
    return merged


def validate(df):
    """Return a list of problems; an empty list means the data is ready."""
    problems = []
    required = ["iso3", "reporter", "partner", "year", "exports_usd_m", "unit"]
    missing_cols = [c for c in required if c not in df.columns]
    if missing_cols:
        return [f"missing columns: {missing_cols}"]
    if (df["exports_usd_m"] < 0).any():
        problems.append("negative values")
    if df["iso3"].isna().any():
        problems.append("unmatched reporters")
    if df.duplicated(["iso3", "partner", "year"]).any():
        problems.append("duplicate keys")
    if not df["year"].between(config.START_YEAR, config.END_YEAR).all():
        problems.append("years out of range")
    if (df["unit"] != "USD millions").any():
        problems.append("mixed units")
    return problems


def summarise(df):
    """Reporting table: World exports by region and year, USD billions."""
    world = df[df["partner"] == "World"]
    return (world.pivot_table(index="region", columns="year", values="exports_usd_m",
                              aggfunc="sum") / 1000).round(1)
