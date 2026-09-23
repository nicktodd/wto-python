# Lab 07: Prepare Raw Data for Analysis

**Duration:** 75 minutes
**Type:** Notebook code exercise

## Objectives
- Profile a raw dataset and list its quality problems
- Standardise text, names, numbers, units and dates
- Handle missing values and duplicates deliberately
- Combine datasets with safe merges
- Validate the result and keep a cleaning log

## Data
- `data/trade_raw_2019_2023.csv`: illustrative exports by reporter and partner region, with deliberate quality problems
- `data/countries.xlsx`: reference country list with ISO3 codes, region and income group
- `data/wb_indicators_2015_2023.csv`: **real** World Bank GDP (Gross Domestic Product) and exports-to-GDP data (CC BY 4.0), built from the Module 05 API responses

## Steps
1. Open `labs/07-data-cleaning-and-transformation/prepare_raw_data.ipynb`.
2. Task 1: profile the raw data and list every problem **before** fixing anything.
3. Task 2: standardise column names, whitespace and reporter names.
4. Task 3: convert values to numbers, standardise units and deal with negatives.
5. Task 4: parse four date formats into a `year` column.
6. Task 5: remove duplicates (exact and by key) and flag missing values.
7. Task 6: merge the country reference data and real World Bank GDP.
8. Task 7: write `validate()`, then save `output/trade_clean.csv` and `output/cleaning_log.txt`.

## Hints
- `df.select_dtypes("object")` selects the text columns.
- `pd.to_numeric(series, errors="coerce")` turns unparseable text into `NaN`.
- `merge(..., validate="many_to_one")` raises an error if the right-hand key is not unique.
- Some duplicates only appear **after** you clean names and dates. Think about why.

## Acceptance criteria
- All check cells print `OK`
- `validate(df)` returns an empty list
- The cleaning log records each change with a row count
