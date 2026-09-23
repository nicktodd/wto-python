# Lab 05: Extract Economic Data from a Public API

**Duration:** 60 minutes
**Type:** Notebook code exercise using real data

## Objectives
- Send HTTP (HyperText Transfer Protocol) requests with the `requests` library
- Understand and navigate JSON (JavaScript Object Notation) responses
- Write a reusable, defensive API function
- Convert API responses into tidy DataFrames and save them with metadata

## Data source
The [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392) is free, public and needs no API key. The data is licensed CC BY 4.0 (Creative Commons Attribution).

| Code | Indicator |
|---|---|
| `NE.EXP.GNFS.ZS` | Exports of goods and services (% of GDP) |
| `NY.GDP.MKTP.CD` | GDP, Gross Domestic Product (current USD) |

**No internet?** Cached responses (retrieved September 2026) are in `data/cache/wb_exports_pct_gdp.json` and `data/cache/wb_gdp_usd.json`. The lab shows you how to fall back to them.

## Setup
```bash
pip install requests
```
(already included in `requirements.txt`)

## Steps
1. Open `labs/05-acquiring-data-from-apis/extract_api.ipynb`.
2. Task 1: make a first request for Kenya and inspect status code, URL and metadata.
3. Task 2: explore the JSON structure of one record.
4. Task 3: write `fetch_indicator()` with a timeout, status check and error detection.
5. Task 4: write `to_frame()` to convert records to a DataFrame.
6. Task 5: extract both indicators for 14 economies, falling back to the cache on network errors, and merge them.
7. Task 6: report missing values, add derived columns, and save CSV plus a metadata JSON file.

## Hints
- The World Bank returns `[metadata, records]`; unpack with `meta, records = resp.json()`.
- An invalid request can return **status 200** with an error message in the body. Check the payload.
- Catch `requests.RequestException` to handle timeouts and connection errors.
- The API can be slow. If a request times out, retry once, then use the cache.

## Acceptance criteria
- All check cells print `OK`
- `output/wb_indicators.csv` has one row per country and year
- `output/wb_indicators_metadata.json` records the source, indicators, date and row count

## Stretch
Register for the [WTO API portal](https://apiportal.wto.org) and read your key from an environment variable. Never commit keys to git.
