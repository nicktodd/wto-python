# Prompt log: example completed version

Responses vary between assistants and runs; this shows the *kind* of progression to expect. The final script is `tariff_extract.py` in this folder (reviewed and tested).

| Round | Prompt | Result | Ran OK? |
|---|---|---|---|
| 1 | `Get tariff data from the World Bank in Python.` | Guessed an indicator (sometimes a non-existent one), one country, printed raw JSON. No error handling. | Partly |
| 2 | "I am an analyst preparing a briefing on applied tariffs for trade policy colleagues. Using Python 3, requests and pandas, get World Bank indicator TM.TAX.MRCH.SM.AR.ZS for AUS BRA CAN CHN DEU IND JPN KEN MEX NGA GBR USA VNM ZAF, 2015-2023. Return a DataFrame with columns iso3, country, year (int), tariff_pct and save it to output/tariffs_wb.csv." | Correct endpoint, but only 50 rows: it used the default page size. | Yes, wrong row count |
| 3a | "The result has 50 rows but should have 126. Fix it, add a 30 second timeout, and raise a clear error if the API returns an error message instead of data." | Added `per_page=1000`, timeout and a payload check. 126 rows. | Yes |
| 3b | "If the request fails, load data/cache/wb_tariff_applied_mean.json instead and log a warning with the logging module." | Added fallback; initially used a path relative to the current folder. | Only from repo root |
| 3c | "Make file paths relative to the script location so it runs from any folder. Keep missing values as NaN; do not fill them." | Used `Path(__file__)`; removed a `fillna(0)` it had silently added in round 2. | Yes |
| 4 | "Restructure into functions fetch_records, to_frame, check, save and main with argparse and an --offline flag. Add docstrings and comments that explain why, not what." | Clean structure as in the final script. | Yes |
| 5 | "List every assumption you have made about the data and the API." | Listed simple vs weighted mean, pagination, missing years, 'World Bank country names may differ from ours'. | n/a |
| 6 | "Act as a critical code reviewer of this script. What could go wrong and how would I test it?" | Suggested retry with back-off, tests for `to_frame` with a `None` value, schema check, logging the API's `lastupdated`. | n/a |

## Assumptions the assistant listed
- Simple (unweighted) mean, not trade-weighted: documented in the module docstring
- All records fit in one page when `per_page` >= total
- Missing values mean "not published", so they are kept as NaN

## Review suggestions accepted / rejected
- **Accepted:** row-count and duplicate check (`check()`), since it catches the pagination bug from round 2
- **Accepted for later:** unit test for `to_frame` (Module 11)
- **Rejected:** retry with exponential back-off; the cache fallback is sufficient for a monthly manual run

## Verification
- Row count: 126 (14 x 9)
- Missing values: some recent years are not yet published, which is expected
- Spot-checks against data.worldbank.org: values match (for example Brazil 2022, 13.29%)
- `--offline` output matches the live run
- Note: the fillna(0) introduced in round 2 would have made unpublished years look like **zero tariffs**. Caught only by reading the code.
