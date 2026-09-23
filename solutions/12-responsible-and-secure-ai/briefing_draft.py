"""Tariff briefing DRAFT generator: redesigned, safer version of briefing_tool.py.

Design choices (see assessment.md):
- Local processing only: no external AI service, no email, no network calls.
- No personal data is read at all.
- Output is a Markdown draft for a human to review, edit, sign off and send.
- The data source and run date are cited in the draft.

Usage (from the repository root):
    python solutions/12-responsible-and-secure-ai/briefing_draft.py
"""
import logging
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
TARIFF_FILE = ROOT / "data" / "tariffs_mfn.csv"
COUNTRIES_FILE = ROOT / "data" / "countries.xlsx"
OUT_FILE = Path(__file__).resolve().parent / "output" / "tariff_briefing_DRAFT.md"
CHANGE_THRESHOLD_PTS = 0.5      # only report changes of at least half a percentage point

log = logging.getLogger("briefing_draft")


def tariff_changes(tariffs, countries):
    """Change in average applied tariff between the two most recent years."""
    latest = tariffs["year"].max()
    prev = latest - 1
    pivot = (tariffs[tariffs["year"].isin([prev, latest])]
             .pivot_table(index=["iso3", "product_code"], columns="year",
                          values="avg_mfn_tariff_pct"))
    pivot["change_pts"] = (pivot[latest] - pivot[prev]).round(2)
    changes = pivot.dropna(subset=["change_pts"]).reset_index()
    changes = changes.merge(countries[["iso3", "country_name"]], on="iso3", how="left")
    big = changes[changes["change_pts"].abs() >= CHANGE_THRESHOLD_PTS]
    log.info("%d of %d country-product pairs changed by >= %.1f points",
             len(big), len(changes), CHANGE_THRESHOLD_PTS)
    return big.sort_values("change_pts", key=abs, ascending=False), prev, latest


def write_draft(changes, prev, latest, path=OUT_FILE):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# DRAFT: Applied tariff changes, {prev} to {latest}",
        "",
        "**Status: DRAFT for human review. Not for circulation.**",
        "",
        f"Source: `{TARIFF_FILE.name}` (illustrative course data). Generated {date.today().isoformat()}.",
        "",
        "| Country | Product group | "
        f"{prev} (%) | {latest} (%) | Change (points) |",
        "|---|---|---|---|---|",
    ]
    for _, r in changes.iterrows():
        lines.append(f"| {r['country_name']} | {r['product_code']} | {r[prev]:.2f} | "
                     f"{r[latest]:.2f} | {r['change_pts']:+.2f} |")
    lines += ["", "## Reviewer checklist",
              "- [ ] Figures checked against the source",
              "- [ ] Interpretation added by the responsible analyst",
              "- [ ] Approved for circulation by: ________"]
    path.write_text("\n".join(lines), encoding="utf-8")
    log.info("Draft written to %s", path)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    tariffs = pd.read_csv(TARIFF_FILE)
    countries = pd.read_excel(COUNTRIES_FILE)
    changes, prev, latest = tariff_changes(tariffs, countries)
    write_draft(changes, prev, latest)


if __name__ == "__main__":
    main()
