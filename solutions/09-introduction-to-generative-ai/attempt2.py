"""Example of a good AI-assisted result for Lab 09 (reviewed and tested).

Prompt used:
    Write a Python script that reads data/trade_summary.csv with pandas.
    Columns: reporter_iso3, reporter, region, year, product_code,
    product_group, exports_usd_m, imports_usd_m.
    Print the five largest exporters in 2023 (total exports across all
    product groups) and each one's share of total 2023 exports, as a
    percentage to one decimal place. Resolve the file path relative to
    this script so it runs from any folder.
"""
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "trade_summary.csv"


def top_exporters(df, year, n=5):
    """Return the n largest exporters in `year` with their share of total exports (%)."""
    in_year = df[df["year"] == year]
    totals = in_year.groupby("reporter")["exports_usd_m"].sum()
    result = pd.DataFrame({
        "exports_usd_m": totals,
        "share_pct": totals / totals.sum() * 100,
    })
    return result.sort_values("exports_usd_m", ascending=False).head(n)


if __name__ == "__main__":
    trade = pd.read_csv(DATA_FILE)
    top5 = top_exporters(trade, 2023)
    print("Top 5 exporters in 2023")
    for reporter, row in top5.iterrows():
        print(f"  {reporter:15} {row['exports_usd_m']:>12,.0f} USD m  {row['share_pct']:5.1f}%")
