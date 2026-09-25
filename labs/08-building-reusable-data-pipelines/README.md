# Lab 08: Create an End-to-End Extraction and Transformation Workflow

**Duration:** 90 minutes (this lab is also the Day 2 consolidation exercise)
**Type:** Python package exercise, built up one function at a time (VS Code or any editor, plus a terminal)

## Objectives
- Structure a pipeline as a small Python package with one module per step
- Reuse your Module 05 and Module 07 code as small, testable functions
- Add logging, validation and command-line options
- Produce a reporting-ready dataset with metadata

## What you are building

```
trade_pipeline/
  config.py        settings: paths, indicators, name map          (complete: read it first)
  extract.py       read files; call the World Bank API            (STEP 10)
  transform.py     clean, merge, validate, summarise              (STEPS 2 to 8)
  load.py          write CSV, Excel and metadata                   (STEP 9)
  run_pipeline.py  arguments, logging, runs everything in order    (STEP 1)
test_steps.py      one group of tests per step
```

Each function you need to write contains a `# TODO STEP n` comment describing exactly what to do. Functions that are already complete (for example `clean_trade()`, which calls your step 2 to 5 functions in order) show you how the pieces fit together.

## How to work
Open a terminal in `labs/08-building-reusable-data-pipelines/` (the folder that **contains** `trade_pipeline/`) with your virtual environment active. For each step:

1. Open the file, find `TODO STEP n`, and replace `raise NotImplementedError` with your code.
2. Run that step's tests:
   ```bash
   pytest test_steps.py -k step01 -v
   ```
3. When they pass, move to the next step.

| Step | File: function | What it does | Reuses |
|---|---|---|---|
| 1 | `run_pipeline.py`: `parse_args`, `setup_logging` | Command-line options; log to console and file | Module 08 slides |
| 2 | `transform.py`: `standardise_text` | Column names, stripping, name map | Lab 07 Part B |
| 3 | `transform.py`: `convert_values` | Numbers, units, negatives | Lab 07 Part C |
| 4 | `transform.py`: `add_year` | Parse four date formats | Lab 07 Part D |
| 5 | `transform.py`: `remove_duplicates` | One row per key | Lab 07 Part E |
| 6 | `transform.py`: `add_reference_data` | ISO3, region, income group | Lab 07 Part F |
| 7 | `transform.py`: `validate` | List of problems | Lab 07 Part G |
| 8 | `transform.py`: `summarise` | Exports by region, USD bn | Lab 04 Part F |
| 9 | `load.py`: `write_outputs` | CSV, Excel, metadata.json | Labs 03 and 05 |
| 10 | `extract.py`: `fetch_wb_indicator` | API with cache fallback | Lab 05 Parts D and E |

## Run the whole pipeline
After step 9 you can run it offline; after step 10, live:

```bash
python -m trade_pipeline.run_pipeline --offline --verbose
python -m trade_pipeline.run_pipeline
python -m trade_pipeline.run_pipeline --help
```

`-m` runs the package as a module so its internal imports (`from . import config`) work.

## Acceptance criteria
- `pytest test_steps.py -v` passes (18 tests)
- `python -m trade_pipeline.run_pipeline --offline` finishes with `Validation passed: 420 rows`
- `trade_pipeline/output/` contains `trade_reporting.csv`, `trade_reporting.xlsx`, `metadata.json` and `pipeline.log`
- A live run fetches from the API, or logs a warning and falls back to the cache

## Stretch
- Add `--start` / `--end` options that override the configured years.
- Save a line chart of the regional summary as `output/exports_by_region.png` using matplotlib.
- Schedule the pipeline with Windows Task Scheduler or cron.
