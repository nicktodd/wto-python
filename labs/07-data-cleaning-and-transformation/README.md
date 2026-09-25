# Lab 07: Prepare Raw Data for Analysis

**Duration:** 75 to 90 minutes
**Type:** Notebook code exercise, built up in small steps

## Objectives
- Profile a raw dataset and list its quality problems
- Standardise names, numbers, units and dates
- Handle duplicates and missing values deliberately
- Combine datasets with safe merges
- Validate the result and keep a cleaning log

## Data
- `data/trade_raw_2019_2023.csv`: illustrative exports by reporter and partner region, with deliberate quality problems
- `data/countries.xlsx`: reference country list with ISO3 codes and income groups
- `data/wb_indicators_2015_2023.csv`: **real** World Bank GDP data (CC BY 4.0), built from the Module 05 API responses

## How this lab works
Open `labs/07-data-cleaning-and-transformation/prepare_raw_data.ipynb`. Each step fixes **one** problem, shows an **Example** where useful, adds a line to your cleaning `log`, and has a **check** cell that prints `OK`.

| Part | You will practise | Steps |
|---|---|---|
| A | Profiling: types, spellings, duplicates; listing the problems | A1 to A4 |
| B | Column names, stripping spaces, finding and mapping name variants | B1 to B4 |
| C | Text to numbers, thousands to millions, negative values | C1 to C4 |
| D | Parsing four date formats into a year | D1 to D3 |
| E | Exact duplicates, duplicate keys, keeping one per key, flagging missing values | E1 to E4 |
| F | Merging reference data and real GDP data | F1 to F2 |
| G | A validation function; saving the data and the log | G1 to G2 |

## Hints
- `pd.to_numeric(series, errors="coerce")` turns unconvertible text into `NaN`.
- `df.loc[mask, "column"] = value` changes only the rows where `mask` is True.
- Some duplicates only appear **after** you clean names and dates. E2 asks you why.

## Acceptance criteria
- Every check cell prints `OK`
- `validate(df)` returns an empty list
- `output/trade_clean.csv` and `output/cleaning_log.txt` exist
