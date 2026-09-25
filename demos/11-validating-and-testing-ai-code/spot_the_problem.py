"""Run the AI-generated yoy_growth on a tiny table where we know the answers.

python spot_the_problem.py          # shows the wrong result
python spot_the_problem.py --fixed  # shows the corrected result
"""
import sys

import pandas as pd

from ai_generated_growth import yoy_growth

trade = pd.DataFrame({
    "reporter": ["Ghana", "Ghana",
                 "Kenya", "Kenya"],
    "year": [2022, 2023, 2022, 2023],
    "exports_usd_m": [17300.0, 16800.0,
                      7950.0, 7412.5],
})


def yoy_growth_fixed(df):
    """Growth within each reporter."""
    totals = (df.groupby(["reporter", "year"])
              ["exports_usd_m"].sum()
              .reset_index())
    totals["growth_pct"] = (
        totals.groupby("reporter")
        ["exports_usd_m"].pct_change()
        * 100).round(1)
    return totals


if __name__ == "__main__":
    fn = yoy_growth_fixed if "--fixed" in sys.argv else yoy_growth
    result = fn(trade)
    print(result[["reporter", "year", "growth_pct"]])
