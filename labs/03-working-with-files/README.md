# Lab 03: Load and Investigate Multiple Datasets

**Duration:** 45 minutes
**Type:** Notebook code exercise

## Objectives
- Navigate folders with `pathlib`
- Read CSV (Comma-Separated Values) files with the `csv` module and with pandas
- Read Excel workbooks and choose a sheet
- Handle missing or unsupported files gracefully
- Write CSV, Excel and text outputs

## Setup
Excel support needs `openpyxl`. It is in `requirements.txt`; if you get an `ImportError`, run:

```bash
pip install openpyxl
```

## Steps
1. Open `labs/03-working-with-files/load_datasets.ipynb`.
2. Task 1: list the files in `data/` with their sizes.
3. Task 2: read `trade_summary.csv` with `csv.DictReader` and total the 2023 exports.
4. Task 3: load all three datasets with pandas and inspect shape and `dtypes`.
5. Task 4: write `load_dataset()` using `try/except`, and load a list of files that includes a missing file and an unsupported file.
6. Task 5: count missing values in each dataset and note which has gaps.
7. Task 6: filter the Africa region for 2023 and write CSV, Excel and a text report to `output/`.

## Hints
- `row["year"]` from `csv.DictReader` is the string `"2023"`, not the number `2023`.
- Filtering a DataFrame on two conditions: `trade[(trade["region"] == "Africa") & (trade["year"] == 2023)]`. We cover this properly in Module 04.
- `Path.suffix` gives the extension, for example `".csv"`.

## Acceptance criteria
- All check cells print `OK`
- `output/` contains `africa_2023.csv`, `africa_2023.xlsx` and `load_report.txt`
