# Lab 05: Extract Economic Data from a Public API

**Duration:** 60 to 75 minutes
**Type:** Notebook code exercise using real data, built up in small steps

## Objectives
- Work with JSON (JavaScript Object Notation) in Python
- Send HTTP (HyperText Transfer Protocol) requests with `requests`
- Turn API records into a tidy DataFrame
- Write a reusable, defensive API function with a cache fallback
- Save data together with metadata about its source

## Data source
The [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392) is free, public and needs no API key (data licence CC BY 4.0).

| Code | Indicator |
|---|---|
| `NE.EXP.GNFS.ZS` | Exports of goods and services (% of GDP) |
| `NY.GDP.MKTP.CD` | GDP, Gross Domestic Product (current USD) |

**No internet?** Cached responses (retrieved September 2026) are in `data/cache/`. Step B2 tells you the line to run instead of the live request, and Part E falls back to the cache automatically.

## How this lab works
Open `labs/05-acquiring-data-from-apis/extract_api.ipynb`. Each step does one thing, shows an **Example**, and has a **check** cell that prints `OK`.

| Part | You will practise | Steps |
|---|---|---|
| A | JSON text to Python; nested dictionaries | A1 to A3 |
| B | Your first request; unpacking the response | B1 to B2 |
| C | Looping over records; counting missing values; building rows; a DataFrame | C1 to C4 |
| D | A reusable function; what a bad request looks like; making it defensive; `to_frame()` | D1 to D4 |
| E | Two indicators with a cache fallback; merging them | E1 to E3 |
| F | Tidying and saving with metadata | F1 to F2 |

## Hints
- The World Bank returns `[metadata, records]`: unpack with `meta, records = resp.json()`.
- An invalid request can return **status 200** with an error message inside. Check the content.
- The API can be slow. If a request times out, re-run it once, then use the cache.

## Acceptance criteria
- Every check cell prints `OK`
- `output/wb_indicators.csv` and `output/wb_indicators_metadata.json` exist

## Stretch
Register for the [WTO API portal](https://apiportal.wto.org) and read your key from an environment variable (`os.environ["WTO_API_KEY"]`). Never put keys in notebooks or git.
