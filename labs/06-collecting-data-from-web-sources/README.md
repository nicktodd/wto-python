# Lab 06: Collect Published Statistical Data from a Website

**Duration:** 60 minutes
**Type:** Notebook code exercise using real data, built up in small steps

## Objectives
- Check whether scraping a page is permitted
- Download a web page politely, with a cache fallback
- Find a table in HTML (HyperText Markup Language) with BeautifulSoup and extract its rows
- Clean scraped values and record where they came from
- Recognise data quality challenges in published web tables

## Data source
Wikipedia, [List of countries by exports](https://en.wikipedia.org/wiki/List_of_countries_by_exports). The figures come from the World Bank. The page text is licensed CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike), so attribute it if you reuse it.

**No internet?** Skip A2 and A3; from Part B the cached copy `data/cache/wikipedia_exports.html` (retrieved September 2026) is used automatically. The live page may differ slightly from the cache.

## How this lab works
Open `labs/06-collecting-data-from-web-sources/scrape_statistics.ipynb`. Each step does one thing, shows an **Example** where useful, and has a **check** cell that prints `OK`.

| Part | You will practise | Steps |
|---|---|---|
| A | robots.txt and other permission checks | A1 to A3 |
| B | Downloading with a fallback | B1 |
| C | Parsing; finding the right table by its caption; header and data rows | C1 to C5 |
| D | Removing footnotes; building a DataFrame; converting types; provenance | D1 to D4 |
| E | `pd.read_html`; mixed reference years; name mismatches; saving | E1 to E4 |

## Legal and ethical checklist
- Is there an API or download instead? Prefer it.
- Do robots.txt and the terms of use allow automated access?
- What licence covers the content, and how must it be attributed?
- Keep request volume low (one request, then cache).
- Does the page contain personal data? If so, stop and check data protection rules.

## Acceptance criteria
- Every check cell prints `OK`
- `output/web_exports.csv` contains clean numeric values plus `source` and `retrieved` columns
