"""Prints the correct answer for the Lab 09 task so you can verify the AI's output.

Run from the repository root:
    python labs/09-introduction-to-generative-ai/check_answer.py
"""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data"

df = pd.read_csv(DATA / "trade_summary.csv")
y2023 = df[df["year"] == 2023]
by_reporter = y2023.groupby("reporter")["exports_usd_m"].sum()
share = by_reporter / by_reporter.sum() * 100
top5 = share.sort_values(ascending=False).head(5).round(1)

print("Expected answer: top 5 exporters in 2023 and share of total 2023 exports (%)")
for reporter, pct in top5.items():
    print(f"  {reporter:15} {pct:5.1f}%")
