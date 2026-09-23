# Lab 08: Create an End-to-End Extraction and Transformation Workflow

**Duration:** 90 minutes (this lab is also the Day 2 consolidation exercise)
**Type:** Python package code exercise (VS Code or any editor, plus a terminal)

## Objectives
- Structure a pipeline as a small Python package with one module per step
- Extract data from a public source (World Bank API) with a cache fallback
- Clean and transform the raw trade data, and merge multiple datasets
- Add logging, validation and command-line options
- Produce a reporting-ready dataset with metadata

## What you are building

```
trade_pipeline/
  config.py        settings: paths, indicators, name map (complete)
  extract.py       read files; call the World Bank API (TODO: fetch_wb_indicator)
  transform.py     clean, merge, validate, summarise (TODO: 4 functions)
  load.py          write CSV, Excel and metadata (TODO: write_outputs)
  run_pipeline.py  logging, arguments, orchestration (TODO: 2 functions)
```

Search for `TODO` in each file. Each has comments describing exactly what to implement. Reuse your Module 05 and Module 07 code.

## Running the pipeline
Open a terminal in `labs/08-building-reusable-data-pipelines/` (the folder that **contains** `trade_pipeline/`) with your virtual environment active:

```bash
python -m trade_pipeline.run_pipeline --offline --verbose
python -m trade_pipeline.run_pipeline
python -m trade_pipeline.run_pipeline --help
```

`-m` runs the package as a module so the relative imports (`from . import config`) work.

## Suggested order
1. Read `config.py` and `run_pipeline.py::run()` to understand the flow.
2. Implement `setup_logging()` and `parse_args()` so you can see log output.
3. Implement `transform.clean_trade()` and `add_reference_data()`; run with `--offline`. Each `NotImplementedError` shows you the next function to write.
4. Implement `validate()` and `summarise()`.
5. Implement `load.write_outputs()`.
6. Implement `extract.fetch_wb_indicator()` and run **without** `--offline` to use the live API.

## Acceptance criteria
- `python -m trade_pipeline.run_pipeline --offline` exits without errors
- `trade_pipeline/output/` contains `trade_reporting.csv`, `trade_reporting.xlsx` (sheets `data`, `exports_by_region_bn`, `metadata`), `metadata.json` and `pipeline.log`
- The log records every cleaning step with a row count
- The dataset has 420 rows (14 reporters x 6 partners x 5 years) and passes `validate()`
- A live run fetches from the API, or logs a warning and falls back to the cache

## Stretch
- Add a `--start` / `--end` option that overrides the configured years.
- Save a line chart of `exports_by_region_bn` as `output/exports_by_region.png` using matplotlib.
- Schedule it with Windows Task Scheduler or cron.
