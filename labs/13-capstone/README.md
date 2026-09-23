# Capstone: Build an AI-Assisted Data Extraction Solution

**Duration:** 2.5 to 3 hours including presentations (optional: run if time allows)
**Type:** Individual or pairs; open-ended project using publicly available international data

## Scenario
Your team has been asked a question that needs data from one or more public international sources. Using everything from the course, and your preferred AI assistant as a pair programmer, build a small, trustworthy solution that extracts, prepares and analyses the data, then present what you found and what you learned about working with AI.

## Activities

| # | Activity | Output | Suggested time |
|---|---|---|---|
| 1 | **Define a data requirement** | `requirement.md` (template provided) | 15 min |
| 2 | **Use AI to help design a Python solution** | Design notes and prompt log | 20 min |
| 3 | **Extract and prepare data** | Script(s) or notebook, clean dataset in `output/` | 60 min |
| 4 | **Validate and test AI-generated code** | At least 5 pytest tests; reconciliation notes | 25 min |
| 5 | **Document the solution** | `SOLUTION.md` (template provided) | 15 min |
| 6 | **Present findings and lessons learned** | 5-minute presentation (outline provided) | 5 min each |

## Data sources (choose at least one; two is better)

| Source | Access | Notes |
|---|---|---|
| [World Bank Open Data](https://data.worldbank.org) | API, no key | Used in Modules 05, 07, 10; cached copies in `data/cache/` |
| [WTO Stats](https://stats.wto.org) / [WTO API](https://apiportal.wto.org) | API, free key | Trade values, tariffs; store your key in an environment variable |
| [UN Comtrade](https://comtradeplus.un.org) | API, free key; bulk downloads | Bilateral trade by HS (Harmonized System) product |
| [IMF Data](https://data.imf.org) | API / downloads | Macroeconomic indicators; some endpoints block scripts, so downloads may be easier |
| [OECD Data Explorer](https://data-explorer.oecd.org) | SDMX API / CSV downloads | Trade in value added, services trade |
| [UN SDG Indicators](https://unstats.un.org/sdgs/dataportal) | API / downloads | e.g. 17.10.1 tariff indicators, 17.11.1 developing country exports |

**No internet?** Use the cached World Bank files in `data/cache/` plus the course datasets in `data/`.

## Example questions (or bring your own)
- Has export openness (exports as % of GDP) risen or fallen for lower middle income economies since 2015?
- Is there a relationship between applied tariff levels and export openness?
- How did the 2020 shock and 2021 recovery differ by region?
- How are developing countries tracking against SDG indicator 17.11.1 (share of global exports)?

## Rules of engagement
- Follow the Module 12 checklist: approved AI tool, no personal or confidential data in prompts.
- Keep a prompt log (reuse `labs/10-prompting-techniques/prompt-log.md`).
- You must be able to explain every line of code you submit.
- Record the source, indicator codes and retrieval date for every dataset.

## Acceptance criteria
- `requirement.md` states a clear question, data sources and definition of done
- The solution runs end to end from a clean checkout (with a cache or offline option)
- At least 5 passing tests, plus one reconciliation against an independent figure
- `SOLUTION.md` explains how to run it, data sources, assumptions and limitations
- A 5-minute presentation covering findings **and** lessons learned about AI-assisted development

A worked example is in `solutions/13-capstone/` for instructors.
