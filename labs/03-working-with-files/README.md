# Lab 03: Load and Investigate Multiple Datasets

**Duration:** 45 to 60 minutes
**Type:** Notebook code exercise, built up in small steps

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

## How this lab works
Open `labs/03-working-with-files/load_datasets.ipynb`. Each step introduces one idea, shows an **Example** of the pattern, and has a **check** cell that prints `OK`. Some cells are marked *Run this cell; no changes needed*: they show you something new before you use it.

| Part | You will practise | Steps |
|---|---|---|
| A | Finding files and their sizes with `pathlib` | A1 to A3 |
| B | Reading a CSV with the `csv` module; counting and totalling in a loop | B1 to B4 |
| C | Reading CSVs with pandas; column types | C1 to C4 |
| D | Reading an Excel workbook and choosing a sheet | D1 to D2 |
| E | `try` / `except`, a safe loader for CSV and Excel, loading a list of files | E1 to E5 |
| F | Creating an output folder; writing CSV, Excel and a text report | F1 to F4 |

## Hints
- A `row["year"]` from `csv.DictReader` is the **text** `"2023"`, not the number `2023`.
- `Path.suffix` gives a file's extension, for example `".csv"`.
- `write()` does not add a newline: end each line with `\n`.

## Acceptance criteria
- Every check cell prints `OK`
- `output/` contains `africa_2023.csv`, `africa_2023.xlsx` and `load_report.txt`
