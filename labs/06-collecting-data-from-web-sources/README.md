# Lab 06: Collect Published Statistical Data from a Website

**Duration:** 60 minutes
**Type:** Notebook code exercise using real data

## Objectives
- Check whether scraping a page is permitted
- Download a web page with a polite User-Agent and a fallback
- Parse HTML (HyperText Markup Language) with BeautifulSoup and extract a table
- Clean scraped values and record provenance
- Identify data quality challenges in published web tables

## Data source
Wikipedia, [List of countries by exports](https://en.wikipedia.org/wiki/List_of_countries_by_exports). The figures come from the World Bank. The page text is licensed CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike), so attribute it if you reuse it.

**No internet?** A cached copy (retrieved September 2026) is at `data/cache/wikipedia_exports.html`. Web pages change, so the live page may differ slightly from the cache.

## Setup
```bash
pip install requests beautifulsoup4 lxml
```
(already included in `requirements.txt`)

## Steps
1. Open `labs/06-collecting-data-from-web-sources/scrape_statistics.ipynb`.
2. Task 1: check robots.txt and list other checks to make before scraping.
3. Task 2: write `get_html()` with a User-Agent, timeout and cache fallback.
4. Task 3: find the table by its caption and extract headers and rows.
5. Task 4: clean footnote markers and separators, convert types, add `source` and `retrieved`.
6. Task 5: compare your result with `pd.read_html`.
7. Task 6: investigate reference years and country name mismatches; save `output/web_exports.csv`.

## Hints
- Use the browser's **Inspect** tool to see the HTML structure of the table.
- `tr.find_all(["th", "td"])` gets every cell in a row, whether header or data.
- `re.sub(r"\[.*?\]", "", text)` removes footnote markers like `[2]`.

## Legal and ethical checklist
- Is there an API or download instead? Prefer it.
- Do robots.txt and the terms of use allow automated access?
- What licence covers the content, and how must it be attributed?
- Are you keeping request volume low (one request, then cache)?
- Does the page contain personal data? If so, stop and check data protection rules.

## Acceptance criteria
- All check cells print `OK`
- `output/web_exports.csv` contains clean numeric values plus `source` and `retrieved` columns
- Data quality notes are written up
