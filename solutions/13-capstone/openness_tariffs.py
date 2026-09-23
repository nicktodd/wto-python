"""Capstone worked example: export openness and applied tariffs, 2015-2023.

Question: how did export openness (exports of goods and services, % of GDP) change
between 2015 and 2023 for the course economies, by income group, and is there a
relationship with applied tariff levels?

Data (real, World Bank, CC BY 4.0):
    NE.EXP.GNFS.ZS        exports of goods and services (% of GDP)
    TM.TAX.MRCH.SM.AR.ZS  tariff rate, applied, simple mean, all products (%)
Reference: data/countries.xlsx (income groups for the course economies).

Usage (from the repository root):
    python solutions/13-capstone/openness_tariffs.py            # live API, cache fallback
    python solutions/13-capstone/openness_tariffs.py --offline  # cached responses only
"""
import argparse
import json
import logging
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "data" / "cache"
OUT = Path(__file__).resolve().parent / "output"
BASE = "https://api.worldbank.org/v2"
START, END = 2015, 2023
INDICATORS = {
    "exports_pct_gdp": ("NE.EXP.GNFS.ZS", "wb_exports_pct_gdp.json"),
    "tariff_pct": ("TM.TAX.MRCH.SM.AR.ZS", "wb_tariff_applied_mean.json"),
}

log = logging.getLogger("capstone")


# ---- extract ---------------------------------------------------------------
def fetch(code, cache_file, iso3_codes, offline=False):
    if not offline:
        url = f"{BASE}/country/{';'.join(iso3_codes)}/indicator/{code}"
        params = {"format": "json", "date": f"{START}:{END}", "per_page": 1000}
        try:
            resp = requests.get(url, params=params, timeout=30)
            resp.raise_for_status()
            payload = resp.json()
            if len(payload) < 2 or not payload[1]:
                raise ValueError(f"no data: {payload[0]}")
            log.info("%s: %d records from API", code, len(payload[1]))
            return payload[1]
        except (requests.RequestException, ValueError) as e:
            log.warning("%s: API failed (%s); using cache", code, e)
    records = json.loads((CACHE / cache_file).read_text(encoding="utf-8"))[1]
    log.info("%s: %d records from cache", code, len(records))
    return records


# ---- transform -------------------------------------------------------------
def records_to_frame(records, column):
    return pd.DataFrame({
        "iso3": [r["countryiso3code"] for r in records],
        "year": [int(r["date"]) for r in records],
        column: pd.to_numeric([r["value"] for r in records]),
    })


def build_panel(frames, countries):
    panel = frames[0]
    for f in frames[1:]:
        panel = panel.merge(f, on=["iso3", "year"], how="outer", validate="one_to_one")
    panel = panel.merge(countries[["iso3", "country_name", "income_group"]],
                        on="iso3", how="left", validate="many_to_one")
    return panel[panel["year"].between(START, END)].sort_values(["iso3", "year"])


def validate(panel, n_countries):
    problems = []
    if panel["income_group"].isna().any():
        problems.append("economies missing from reference data")
    if panel.duplicated(["iso3", "year"]).any():
        problems.append("duplicate country-years")
    if panel["iso3"].nunique() != n_countries:
        problems.append("unexpected number of economies")
    if (panel["exports_pct_gdp"] < 0).any() or (panel["tariff_pct"] < 0).any():
        problems.append("negative percentages")
    return problems


# ---- analyse ---------------------------------------------------------------
def openness_change(panel):
    """Exports % of GDP in the first and last year, and the change, per economy."""
    wide = panel.pivot_table(index=["country_name", "income_group"], columns="year",
                             values="exports_pct_gdp")
    out = wide[[START, END]].copy()
    out["change_pts"] = out[END] - out[START]
    return out.round(1).sort_values("change_pts")


def by_income_group(panel):
    """Average openness and tariff by income group and year (simple, unweighted means)."""
    return (panel.groupby(["income_group", "year"])[["exports_pct_gdp", "tariff_pct"]]
                 .mean().round(1).unstack("year"))


def tariff_openness_correlation(panel):
    """Pearson correlation of country averages (a descriptive statistic, not causation)."""
    avg = panel.groupby("iso3")[["exports_pct_gdp", "tariff_pct"]].mean().dropna()
    return round(avg["exports_pct_gdp"].corr(avg["tariff_pct"]), 2), len(avg)


# ---- load ------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Export openness and tariffs")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    countries = pd.read_excel(ROOT / "data" / "countries.xlsx")
    iso3 = sorted(countries["iso3"])
    frames = [records_to_frame(fetch(code, cache, iso3, args.offline), col)
              for col, (code, cache) in INDICATORS.items()]
    panel = build_panel(frames, countries)

    problems = validate(panel, len(iso3))
    if problems:
        raise SystemExit(f"Validation failed: {problems}")
    log.info("Panel: %d rows; missing exports %d, missing tariffs %d", len(panel),
             panel["exports_pct_gdp"].isna().sum(), panel["tariff_pct"].isna().sum())

    OUT.mkdir(exist_ok=True)
    change = openness_change(panel)
    groups = by_income_group(panel)
    corr, n = tariff_openness_correlation(panel)
    panel.to_csv(OUT / "panel.csv", index=False)
    with pd.ExcelWriter(OUT / "capstone_results.xlsx") as xl:
        change.to_excel(xl, sheet_name="openness_change")
        groups.to_excel(xl, sheet_name="by_income_group")
        panel.to_excel(xl, sheet_name="data", index=False)

    print("\nChange in exports as % of GDP, 2015 to 2023:\n", change)
    print(f"\nCorrelation of average tariff with average openness: {corr} (n={n} economies)")


if __name__ == "__main__":
    main()
