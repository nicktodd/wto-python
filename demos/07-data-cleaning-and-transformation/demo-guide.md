# Demo: Module 07: Data Cleaning and Transformation

**Duration:** 12 minutes
**Prerequisite:** JupyterLab open at `demos/07-data-cleaning-and-transformation/cleaning.ipynb`. Also open `data/trade_raw_2019_2023.csv` in Excel or a text editor so delegates can see the raw mess.

## Part 1: Meet the mess (2 min)
Show the CSV in Excel. Point at: `USA` / `U.S.` / `united states `, `Dec 2021` vs `31/12/2021`, `1,234.5`, `n/a`, the `USD thousands` rows.
Run the first cell: `Value` is `object` (text) because of those values. "One bad value turns a whole column into text."

## Part 2: Standardise (3 min)
- Strip, then `value_counts()` to reveal variants.
- The `NAME_MAP` dictionary: "Mapping tables are how statistical offices do this at scale; ISO3 (three-letter ISO) codes are the real fix."
- `pd.to_numeric(errors="coerce")`: bad values become `NaN` (Not a Number), so you can count them.

## Part 3: Missing values, duplicates, units (3 min)
- Missing values: drop, fill or flag. "In official statistics we rarely invent numbers: flag and report."
- Duplicates: exact duplicates first, then duplicate **keys**.
- Units: convert thousands to millions **before** any aggregation.

## Part 4: Dates, combine, validate (4 min)
- `parse_period` tries each format in turn.
- Merge to `countries.xlsx` with `validate="many_to_one"` and `indicator=True`: "merge problems are the most common silent error in analysis."
- Merge real World Bank GDP (Gross Domestic Product) data.
- The `validate()` function: "Write your assumptions down as code, and run them every time."

## Key message
Cleaning is where analytical accuracy is won or lost: make every fix explicit, count what it affects, and validate the result.
