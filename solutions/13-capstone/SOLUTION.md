# Solution: Export openness and applied tariffs, 2015-2023 (worked example)

## Summary
Question: how did export openness (exports of goods and services as % of GDP) change between 2015 and 2023 for the 14 course economies, and is it related to applied tariff levels? Openness rose for 11 of the 13 economies with data, most strongly for Viet Nam (+13.8 points). China and the United States fell slightly. Across economies, higher average applied tariffs are weakly associated with lower openness (correlation -0.28, n = 13), but this is descriptive only and heavily influenced by a few economies.

## How to run
```bash
python solutions/13-capstone/openness_tariffs.py            # live API with cache fallback
python solutions/13-capstone/openness_tariffs.py --offline  # cached responses only
pytest solutions/13-capstone -v
```
Outputs: `output/panel.csv` and `output/capstone_results.xlsx` (sheets `openness_change`, `by_income_group`, `data`).

## Data sources
| Source | Indicator | Retrieved | Licence |
|---|---|---|---|
| World Bank | NE.EXP.GNFS.ZS, exports of goods and services (% of GDP) | September 2026 (cache) | CC BY 4.0 |
| World Bank | TM.TAX.MRCH.SM.AR.ZS, tariff rate, applied, simple mean, all products (%) | September 2026 (cache) | CC BY 4.0 |
| Course reference | `data/countries.xlsx` income groups | n/a | Illustrative |

## Processing steps
1. **Extract:** World Bank API for both indicators and all 14 ISO3 codes, 2015-2023; cached JSON fallback.
2. **Transform:** records to tidy frames; outer merge on ISO3 and year (`validate="one_to_one"`); add income group (`many_to_one`).
3. **Validate:** no unknown economies, no duplicate country-years, expected count of economies, no negative percentages.
4. **Analyse:** change 2015 to 2023 per economy; unweighted means by income group and year; correlation of country averages.

## Validation and testing
- 6 pytest tests: missing-value handling, merge and validation, change calculation, correlation input, cache shape (126 records = 14 x 9).
- Reconciliation: spot-check two values against the data.worldbank.org website, for example Brazil tariff 2022 (13.29%).

## Assumptions and limitations
- **Nigeria** has no exports-to-GDP data for 2015-2023 in the source, so it is excluded from the openness results.
- **Tariffs for 2023** were not yet published at retrieval; Mexico and Nigeria have only 5 tariff years.
- Income-group averages are **unweighted** and composition changes when data is missing.
- Openness includes services; the tariff measure covers merchandise only.
- Correlation of 13 country averages is not evidence of causation, and small samples are sensitive to outliers (Viet Nam).

## Use of AI (illustrative account for this example)
- Tool: an approved AI assistant, used for the design outline, the first draft of `fetch()` and the test ideas.
- Errors caught: the first draft used the default page size (50 records, not 126), found by the cache-shape test and a row-count check; it also filled missing tariffs with zero, found in code review.
- Prompt log: kept alongside the project (see the Module 10 format).

## Presentation outline
1. Question: are more open economies lower-tariff economies, and how has openness changed?
2. Data: two World Bank indicators, 14 economies, 2015-2023; pipeline diagram
3. Findings: openness change table; the -0.28 correlation with caveats
4. Validation: tests, spot-checks, documented gaps (Nigeria, 2023 tariffs)
5. AI lessons: fast first drafts; pagination and missing-value errors only caught by checks
