# Data requirement (worked example)

## 1. The question
How did export openness change between 2015 and 2023 for the 14 course economies, by income group, and is openness related to applied tariff levels? Audience: trade policy colleagues preparing background for a discussion on tariffs and development.

## 2. Scope
- Economies: the 14 in `data/countries.xlsx`
- Years: 2015-2023
- Products: all (openness covers goods and services; tariffs cover merchandise)
- Measures: exports % of GDP; applied tariff, simple mean, %

## 3. Data sources
| Source | Code | Access | Licence |
|---|---|---|---|
| World Bank | NE.EXP.GNFS.ZS | API, no key; cache in `data/cache/` | CC BY 4.0 |
| World Bank | TM.TAX.MRCH.SM.AR.ZS | API, no key; cache in `data/cache/` | CC BY 4.0 |

## 4. Definitions and assumptions
- Export openness = NE.EXP.GNFS.ZS.
- Tariff = simple (unweighted) mean applied rate; not trade-weighted.
- Missing values are left missing, never filled.

## 5. Definition of done
- Table of 2015 vs 2023 openness per economy; income-group averages by year; one correlation with caveats
- Excel and CSV outputs; at least 5 passing tests; two values spot-checked on data.worldbank.org

## 6. Risks
API slow or unavailable (use the cache); data gaps for some economies and the latest year; the temptation to over-interpret a correlation.
