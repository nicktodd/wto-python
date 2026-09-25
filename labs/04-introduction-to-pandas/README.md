# Lab 04: Analyse Trade Data with pandas

**Duration:** 75 to 90 minutes (this lab also consolidates Modules 01 to 04)
**Type:** Notebook code exercise, built up in small steps

## Objectives
- Load several datasets into DataFrames
- Select, filter and sort
- Create calculated fields
- Group and summarise, including pivot tables
- Check data quality, combine datasets and produce a summary report

## How this lab works
Open `labs/04-introduction-to-pandas/trade_analysis.ipynb`. Each step does one thing, shows an **Example** of the pattern (the same pattern as on the slides and in `demos/04-introduction-to-pandas/pandas_intro.ipynb`), and has a **check** cell that prints `OK`.

| Part | You will practise | Steps |
|---|---|---|
| A | Loading three datasets; `info()` | A1 to A3 |
| B | Selecting one column, several columns; statistics on a column | B1 to B3 |
| C | Filtering with one condition, two conditions, `loc`, a numeric condition | C1 to C4 |
| D | Sorting and top N | D1 to D2 |
| E | Calculated columns: balance, billions, True/False | E1 to E3 |
| F | `groupby`, top five, `pivot_table`, growth, shares | F1 to F5 |
| G | Missing values, duplicates, impossible values | G1 |
| H | Merge country data; totals by income group; a multi-sheet Excel report | H1 to H3 |

## Hints
- Double brackets select several columns: `trade[["reporter", "year"]]`.
- Combine filters with `&` and wrap **each** condition in brackets.
- In a pivot with years as columns, `totals[2023]` is the 2023 column.

## Acceptance criteria
- Every check cell prints `OK`
- `output/day1_summary.xlsx` opens in Excel with four sheets
- Data quality findings and three management findings are written up
