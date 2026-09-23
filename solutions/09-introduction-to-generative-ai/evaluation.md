# Lab 09 evaluation record: example completed version

**AI assistant used:** (any approved assistant)
**Date:** example

## Attempt 1: vague prompt

**Prompt:** `Write Python to find the top exporters.`

**What did the assistant assume?** A typical response invents a file name (for example `trade_data.csv`) and column names (`country`, `exports`), picks no particular year, and often ranks individual rows rather than totals per country. It usually does not run against our data without edits. The assistant is not wrong so much as **under-informed**: it filled every gap with a guess.

## Attempt 2: specific prompt

**Prompt:** see the docstring in `attempt2.py`.

## Evaluation

| # | Question | Result | Evidence |
|---|---|---|---|
| 1 | Does it run? | Pass | Runs from the repository root and from its own folder, because the path is resolved relative to the script. |
| 2 | Answers the question asked? | Pass | Filters to 2023, sums across product groups per reporter, top 5, share to 1 dp. |
| 3 | Is the answer right? | Pass | Identical to `check_answer.py`. (A common failure: ranking single product rows, so China appears once for Manufactures and the top 5 is wrong.) |
| 4 | Functions and APIs exist? | Pass | `read_csv`, `groupby`, `sum`, `sort_values`, `head`, `iterrows` all in the pandas docs. |
| 5 | Hidden assumptions? | Note | Share is of the 14 economies in the file, not of world exports. Values are nominal USD millions and illustrative. Should be stated in any output. |
| 6 | Readable and maintainable? | Pass | Logic in a named, documented function that can be tested; `__main__` guard. |
| 7 | Safe? | Pass | Reads a local file only; no secrets, no network calls. |
| 8 | Would I sign my name to it? | Yes, with the caveat in row 5 written into the output. |

## Hallucination hunt (example findings)

| Question | Typical answer | Official source | Hallucinated? |
|---|---|---|---|
| World Bank code for exports % of GDP | `NE.EXP.GNFS.ZS` | data.worldbank.org confirms | No |
| WTO Timeseries API parameters | Often invents simple endpoints such as `/v1/trade?reporter=...`; the real API uses `/timeseries/v1/data` with indicator codes and needs a subscription key | apiportal.wto.org | Often yes |
| pandas function to combine on a column | `merge` (sometimes `join`, which joins on the index by default) | pandas docs | Partly: `join` needs care |

## Reflection (example)
1. It produced a working, well-structured script in seconds and explained pandas syntax clearly.
2. Without `check_answer.py`, the row-level ranking error in some responses would have looked plausible.
3. Always give file paths, column names, definitions ("total across product groups") and the expected output format; always ask how to verify the result.
