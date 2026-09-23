"""Export summary report: reviewed, tested and corrected version.

See review.md in this folder for the list of errors found in the AI-generated original.
"""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"          # fix 1: not relative to cwd
TRADE_FILE = DATA / "trade_summary.csv"
TARIFF_FILE = DATA / "tariffs_mfn.csv"


def load_data(trade_file=TRADE_FILE, tariff_file=TARIFF_FILE):
    """Load the trade and tariff datasets."""
    return pd.read_csv(trade_file), pd.read_csv(tariff_file)


def total_exports(df, year):
    """Total exports across all reporters and products for a year, USD millions."""
    return df.loc[df["year"] == year, "exports_usd_m"].sum()           # fix 2: sum, not mean


def growth_rate(old, new):
    """Percentage growth from old to new; NaN when old is zero (growth undefined)."""
    if pd.api.types.is_scalar(old):
        return float("nan") if old == 0 else (new - old) / old * 100
    return (new - old) / old.where(old != 0) * 100                      # fix 3: divide by old


def export_growth(df, start, end):
    """Growth (%) of each reporter's total exports between two years."""
    totals = df.groupby(["reporter", "year"])["exports_usd_m"].sum().unstack()
    return growth_rate(totals[start], totals[end]).round(1)


def agricultural_share(df, year):
    """Agricultural products as a percentage of each reporter's exports."""
    y = df[df["year"] == year]
    agr = y[y["product_code"] == "AGR"].groupby("reporter")["exports_usd_m"].sum()
    total = y.groupby("reporter")["exports_usd_m"].sum()
    return (agr.reindex(total.index, fill_value=0) / total * 100).round(1)   # fix 4: x 100


def trade_balance(df, year):
    """Exports minus imports for each reporter, USD millions."""
    y = df[df["year"] == year].groupby("reporter")
    return y["exports_usd_m"].sum() - y["imports_usd_m"].sum()          # fix 5: sign


def top_exporters(df, year, n=5):
    """The n largest exporters in a year, by total exports."""
    totals = df[df["year"] == year].groupby("reporter")["exports_usd_m"].sum()
    return totals.sort_values(ascending=False).head(n)                  # fix 6: largest first


def average_tariff(tariffs, iso3):
    """Average applied tariff (%) for a country, ignoring missing values."""
    return tariffs.loc[tariffs["iso3"] == iso3, "avg_mfn_tariff_pct"].mean()  # fix 7: no fillna(0)


def exports_by_region(df, year):
    """Total exports by region for a year, USD billions."""
    y = df[df["year"] == year]
    return (y.groupby("region")["exports_usd_m"].sum() / 1_000).round(1)   # fix 8: millions -> billions


if __name__ == "__main__":
    trade, tariffs = load_data()
    print(f"Total 2023 exports: {total_exports(trade, 2023):,.0f} USD m")
    print("\nTop 5 exporters, 2023:\n", top_exporters(trade, 2023))
    print("\nExport growth 2019-2023 (%):\n", export_growth(trade, 2019, 2023))
    print("\nExports by region, 2023 (USD bn):\n", exports_by_region(trade, 2023))

    report = pd.DataFrame(                                                 # fix 9: no DataFrame.append
        [{"iso3": iso3, "avg_tariff": average_tariff(tariffs, iso3)}
         for iso3 in tariffs["iso3"].unique()]
    ).round(2)
    print("\nAverage tariffs:\n", report)
