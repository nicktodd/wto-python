# Demo: Module 06: Collecting Data from Web Sources

**Duration:** 12 minutes
**Prerequisite:** JupyterLab open at `demos/06-collecting-data-from-web-sources/scrape_exports.ipynb`. Also open https://en.wikipedia.org/wiki/List_of_countries_by_exports in a browser. If there is no internet, run the *Offline fallback* section first and continue from *Parsing the real page*.

The demo notebook has one `##` section per code slide, in slide order: run each section as you reach its slide. The sections below are the highlights to talk through.

## Part 0: A tiny table first (3 min)
Run the four *tiny HTML table* sections. Show the six lines of HTML, then `find`, `find_all` and `get_text` on it. "Learn the tools where you can see everything; then the real page is just bigger."

## Part 1: Look before you scrape (3 min)
- In the browser, right-click the exports table and choose **Inspect**. Show `<table class="wikitable">`, `<caption>`, `<tr>`, `<th>` and `<td>`.
- Run the robots.txt cell. Explain that we download robots.txt with `requests` and our own User-Agent because Python's built-in `RobotFileParser.read()` gets blocked by some sites, which makes it wrongly report "not allowed".
- Talking point: robots.txt is a courtesy signal, not the whole legal picture. Terms of use, copyright and data protection law also apply.

## Part 2: Download and parse (4 min)
- Show the status code and `Content-Type: text/html`.
- `soup.title`, then find the table by its class, then show the caption: "Always confirm you have the right table and note its units: US$ million."
- Extract rows into a list of lists.

## Part 3: Clean and the shortcut (3 min)
- Convert types; remove the thousands separators.
- Then show `pd.read_html`: "one line, but you still have to check what it gives you."

## Part 4: Data quality (2 min)
Run the year check: countries have **different reference years**. Ask: "Is it fair to rank a country on 2021 data against another on 2024 data?"

## Key message
Scraping is a last resort after checking for an API or download: get permission, identify the right table, clean it, and record exactly where and when the data came from.
