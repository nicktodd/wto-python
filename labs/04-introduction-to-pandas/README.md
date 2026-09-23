# Lab 04: Analyse Trade Data with pandas

**Duration:** 75 minutes (this lab is also the Day 1 consolidation exercise)
**Type:** Notebook code exercise

## Objectives
- Load several datasets into DataFrames
- Explore data quality issues
- Select, filter and sort records
- Create calculated fields
- Produce grouped summary statistics and a summary report

## Steps
1. Open `labs/04-introduction-to-pandas/trade_analysis.ipynb`.
2. **Part A:** load `trade_summary.csv`, `tariffs_mfn.csv` and `countries.xlsx`.
3. **Part B:** investigate types, missing values, duplicates, value ranges and categories. Write down your findings.
4. **Part C:** select the Kenya rows, sort 2023 Manufactures exports, count large importers.
5. **Part D:** add trade balance, exports in billions, and each product's share of the reporter's exports.
6. **Part E:** build four summaries: region by year, top 5 exporters, 2019-2023 growth and agricultural share.
7. **Part F:** merge the countries reference data and summarise by income group. Stretch: add tariffs.
8. **Part G:** write all summaries to `output/day1_summary.xlsx` (one sheet each) and write three findings for a manager.

## Hints
- Combine filters with `&` (and) or `|` (or), and wrap each condition in brackets.
- `groupby(...).transform("sum")` returns a group total aligned to every row.
- `pivot_table(index=..., columns=..., values=..., aggfunc="sum")` builds a cross-tab.
- In a pivot with years as columns, `totals[2023] / totals[2019] - 1` gives growth.

## Acceptance criteria
- All check cells print `OK`
- `output/day1_summary.xlsx` opens in Excel with four sheets
- Data quality findings and three management findings are written up
