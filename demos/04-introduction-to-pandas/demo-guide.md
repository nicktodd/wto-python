# Demo: Module 04: Introduction to pandas

**Duration:** 12 minutes (run each section after its slide)
**Prerequisite:** JupyterLab open at `demos/04-introduction-to-pandas/pandas_intro.ipynb`.

## Part 1: DataFrames and Series (2 min)
Run `trade.info()`. Point out the row count, the column types and "non-null" counts: "info() is the first thing to run on any new dataset."
Show that one column is a `Series`, then `describe()`.

## Part 2: Select, filter, sort (4 min)
- Double brackets select several columns; `loc` is by label, `iloc` by position.
- Filtering: say the boolean mask out loud: "keep rows where region equals Africa."
- Common mistake: using `and` instead of `&`, or forgetting brackets around each condition. Show the error live.
- `query()` as a readable alternative.
- Sorting: chain `sort_values` and `head` for a top 5.

## Part 3: Calculated fields (2 min)
Create `balance_usd_m`. "Whole-column arithmetic: no loops needed. This is the big step up from Module 02."

## Part 4: Group and summarise (4 min)
- `groupby` + `sum` = pivot table. `agg` with named outputs for several statistics at once.
- `pivot_table` + `pct_change(axis=1)`: year-on-year growth for every country in one statement. Point at 2020.
- Preview the merge with `countries.xlsx`: "We will do this properly on Day 2."

## Key message
pandas works on whole columns at once: select, filter, calculate and group replace hundreds of spreadsheet formulas with a few readable lines.
