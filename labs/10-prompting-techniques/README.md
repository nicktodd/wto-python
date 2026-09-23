# Lab 10: Generate and Refine a Data Extraction Script with Prompt Engineering

**Duration:** 60 minutes
**Type:** Guided exercise using your preferred AI assistant

## Objectives
- Write prompts that include business context, data details, format and constraints
- Improve code through iterative prompting rather than starting again
- Ask the assistant for explanations, documentation and a self-review
- Keep a prompt log that makes your AI-assisted work reproducible

## Scenario
A trade policy team wants a reusable script that extracts the World Bank's **applied tariff rate, simple mean, all products (%)**, indicator `TM.TAX.MRCH.SM.AR.ZS`, for the 14 economies in our course dataset, 2015 to 2023, ready to combine with the trade data. You will build it **only by prompting** your AI assistant, then review what it produced.

If the API is unreachable, a cached response is in `data/cache/wb_tariff_applied_mean.json`.

## Setup
- Use your preferred approved AI assistant in VS Code or in a browser.
- Open `prompt-patterns.md` from `demos/10-prompting-techniques/` for reference.
- Open `prompt-log.md` in this folder and record **every** prompt and a one-line note on the result.
- Save the script as `labs/10-prompting-techniques/tariff_extract.py`.

## Steps
Run the script after **every** round, and note what changed in the prompt log.

1. **Round 1: baseline.** Write a one-sentence prompt. Run whatever you get. Note the problems.
2. **Round 2: context and specifics.** Start a new chat. Use the CRAFT checklist: who it is for, the indicator code, the 14 ISO3 codes (`AUS BRA CAN CHN DEU IND JPN KEN MEX NGA GBR USA VNM ZAF`), years, and the output: a DataFrame with columns `iso3`, `country`, `year` (int), `tariff_pct`, saved to `output/tariffs_wb.csv`.
3. **Round 3: robustness.** In the same chat, one requirement per prompt:
   - a timeout and clear error if the API returns an error message instead of data
   - a fallback to the cached JSON file, with a logged warning
   - keep missing values as missing (no filling)
4. **Round 4: structure and documentation.** Ask for functions (extract, transform, save, main), docstrings, comments explaining *why*, and a command-line option `--offline`.
5. **Round 5: explanation and assumptions.** Ask the assistant to list every assumption it made and explain any line you do not understand.
6. **Round 6: self-review.** Ask it to act as a critical reviewer of its own code. Decide which suggestions to accept, and say why in your log.
7. **Verify** the output yourself:
   - 14 countries x 9 years = 126 rows?
   - Spot-check two values against https://data.worldbank.org/indicator/TM.TAX.MRCH.SM.AR.ZS
   - Run with `--offline` and compare.

## Acceptance criteria
- `python labs/10-prompting-techniques/tariff_extract.py` produces `output/tariffs_wb.csv` with 126 rows and the four required columns
- `--offline` works using the cached file
- `prompt-log.md` shows at least six prompts, with a note on each result
- You can explain every line of the final script

## Stretch
Ask the assistant to merge the tariffs with `data/trade_summary.csv` (on ISO3 code and year) and calculate the correlation between tariff level and import growth. Be sceptical: what does the correlation *not* tell you?
