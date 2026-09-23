# Demo: Module 03: Working with Files

**Duration:** 10 minutes
**Prerequisite:** JupyterLab open at `demos/03-working-with-files/files.ipynb`. Delete any `output/` folder left over from a previous run.

## Part 1: Paths (2 min)
Run the `pathlib` cell. Explain `../../data`: "two folders up from this notebook, then into data."
Show `DATA.resolve()` printing the absolute path. "Relative paths make the project portable: it works on anyone's laptop."

## Part 2: CSV two ways (3 min)
- `csv.DictReader`: every value arrives as a **string**. Point at the `<class 'str'>` output.
- `pd.read_csv`: pandas infers types. Show `dtypes`: `int64`, `float64`, `object` (text).

## Part 3: Excel (2 min)
Show `sheet_names`, then `read_excel(..., sheet_name="countries")`. Mention that `openpyxl` must be installed (it is in `requirements.txt`).

## Part 4: Writing and errors (3 min)
- Run the write cell, then open `output/kenya.xlsx` in Excel to prove the round trip.
- Run `load_csv` on a missing file. Then temporarily remove the `try/except` to show the raw `FileNotFoundError` traceback, and put it back.

## Key message
Read with the right tool, write results somewhere predictable, and expect files to be missing or broken.
