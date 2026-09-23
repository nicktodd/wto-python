# Module 09 demo prompts

Use these in **your organisation's approved AI assistant** (for example GitHub Copilot Chat, ChatGPT, Claude or Microsoft Copilot). Paste them exactly as written so the class sees an unedited response.

## Prompt 1: A deliberately vague prompt
```
Write Python to analyse trade data.
```

## Prompt 2: A specific prompt
```
Write a Python script that reads data/trade_summary.csv with pandas.
Columns: reporter_iso3, reporter, region, year, product_code,
product_group, exports_usd_m, imports_usd_m.
Print the five largest exporters in 2023 (total exports across all
product groups) and each one's share of total 2023 exports, as a
percentage to one decimal place.
```

## Prompt 3: Ask for an explanation
```
Explain what each line of that script does, for someone who
started learning Python two days ago.
```

## Prompt 4: Probe for hallucination
```
What is the URL of the WTO API endpoint for merchandise exports by
country, and what parameters does it take?
```
Then open https://apiportal.wto.org and compare. Point out any invented detail and whether the assistant stated its uncertainty.

## Prompt 5: A fact check
```
In what year did Kenya join the WTO?
```
The correct answer is 1995 (Kenya is an original member). Discuss: whatever the assistant said, how would you check it?
