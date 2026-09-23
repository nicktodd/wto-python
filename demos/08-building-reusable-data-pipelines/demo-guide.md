# Demo: Module 08: Building Reusable Data Pipelines

**Duration:** 12 minutes
**Prerequisite:** VS Code (Visual Studio Code) or JupyterLab's text editor open at `demos/08-building-reusable-data-pipelines/wb_pipeline.py`, and a terminal with the virtual environment activated, in the same folder.

## Part 1: Tour the script (4 min)
Scroll through `wb_pipeline.py` top to bottom:
- Docstring with usage, imports, configuration constants.
- One function per step: `extract`, `transform`, `validate`, `load`.
- `main()` reads like a table of contents for the pipeline.
- The `if __name__ == "__main__":` guard. "This lets us import the functions into a test without running the pipeline."

## Part 2: Run it (3 min)
```bash
python wb_pipeline.py
python wb_pipeline.py --start 2020 --end 2023
python wb_pipeline.py --help
```
Show the console log, then open `output/run.log` and `output/exports_pct_gdp.csv`.

## Part 3: Break it on purpose (3 min)
- Turn Wi-Fi off (or change `BASE` to a wrong host) and run again: the WARNING line shows the cache fallback. "The run still succeeds, and the log says why."
- Change `COUNTRIES` to add `"XXX"`, run again: validation stops the run. "Better to fail loudly than to publish wrong numbers." Undo the change.

## Part 4: Automation (2 min)
Show how Windows Task Scheduler (or cron on Linux and macOS) could run `python wb_pipeline.py` monthly. Mention that the lab pipeline returns a non-zero exit code on failure so a scheduler can raise an alert.

## Key message
A pipeline is a notebook grown up: configuration in one place, one function per step, logging throughout and validation before anything is published.
