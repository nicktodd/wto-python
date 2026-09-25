# Demo: Module 05: Acquiring Data from External Sources

**Duration:** 12 minutes
**Prerequisite:** JupyterLab open at `demos/05-acquiring-data-from-apis/world_bank_api.ipynb`. Test internet access before the session. The World Bank API is free but sometimes slow; if it times out, use the cache fallback cell and make that the teaching point.

The demo notebook has one `##` section per code slide, in slide order: run each section as you reach its slide. The sections below are the highlights to talk through.

## Part 0: Setup check (2 min)
Ask delegates to activate their virtual environment, run `jupyter lab`, and run the first cell of this notebook. Fix any environment problems now, not mid-lab.

## Part 1: JSON (2 min)
Run the JSON cell. "JSON (JavaScript Object Notation) maps directly onto Python: objects become dictionaries, arrays become lists."

## Part 2: A real request (3 min)
- Paste the printed `resp.url` into a browser to show that an API is "just a URL that returns data."
- Show `params` building the query string for you.
- Explain status codes: 200 OK, 404 Not Found, 429 Too Many Requests, 500 Server Error.

## Part 3: Inspect and convert (3 min)
- The World Bank returns a two-element list: `[metadata, records]`. Point out `pages`, `per_page` and `total`.
- Note that `value` can be `None` for years not yet published.
- Build the DataFrame with a list comprehension.

## Part 4: Defensive code (2 min)
- Walk through `fetch_indicator`: timeout, `raise_for_status`, and checking the payload.
- Run the `XXX` request: **status 200, but the body is an error message**. "Never trust the status code alone."
- Show the cache fallback. Remind delegates that API keys (WTO, UN Comtrade) belong in environment variables, never in notebooks or git.

## Key message
An API is a URL that returns structured data: request it with parameters, check the response carefully, and always have a fallback.
