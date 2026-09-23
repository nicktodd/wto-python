"""AI-generated helpers (demo). Review them!"""
import pandas as pd


def yoy_growth(df):
    """Year-on-year export growth (%) for each
    reporter, from a trade_summary table."""
    totals = (df.groupby(["reporter", "year"])
              ["exports_usd_m"].sum()
              .reset_index())
    totals["growth_pct"] = (
        totals["exports_usd_m"].pct_change()
        * 100).round(1)
    return totals


def share_of_total(df, year):
    """Each reporter's share of exports (%)."""
    y = df[df["year"] == year]
    s = y.groupby("reporter")["exports_usd_m"]
    return (s.sum() / y["exports_usd_m"].sum()
            * 100).round(1)


if __name__ == "__main__":
    trade = pd.read_csv("../../data/trade_summary.csv")
    print(yoy_growth(trade).head(12))
