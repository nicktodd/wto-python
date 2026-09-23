# Code review: export_summary.py (instructor answer key)

| # | Function | Problem | Typically found by | Fix |
|---|---|---|---|---|
| 1 | module constants | `"data/trade_summary.csv"` is relative to the **current folder**, so the script only works when run from the repository root | Running from the lab folder | Build paths from `Path(__file__).resolve()` |
| 2 | `total_exports` | Uses `.mean()` although the docstring promises a **total**. Output is plausible (a large number), so easy to miss | Test with known totals; reconciling with an Excel pivot | `.sum()` |
| 3 | `growth_rate` | Divides by `new` instead of `old`: 100 to 110 gives 9.1% not 10%. Also divides by zero when `old` is 0 | Test with 100 -> 110; edge case 0 -> 5 | `(new - old) / old * 100`; return NaN when `old == 0` |
| 4 | `agricultural_share` | Returns a fraction (0.2) although the docstring says percentage | Reading docstring vs code; test | Multiply by 100 |
| 5 | `trade_balance` | Imports minus exports: the **sign is reversed**, so surpluses appear as deficits | Reading docstring vs code; test with a known surplus | Exports minus imports |
| 6 | `top_exporters` | `sort_values()` is ascending, so it returns the **smallest** five | Running (Kenya in a "top 5"); test | `ascending=False` |
| 7 | `average_tariff` | `fillna(0)` treats unpublished tariffs as **zero**, biasing averages down, contrary to the docstring | Reading; test with a NaN in the fixture | Remove `fillna(0)`: `mean()` already skips NaN |
| 8 | `exports_by_region` | Divides USD millions by 1,000,000, giving **trillions**, labelled billions | Reconciliation: region totals do not add up to total exports | Divide by 1,000 |
| 9 | `__main__` | `DataFrame.append` was removed in pandas 2.0: a typical outdated-training-data error | Running (AttributeError) | Build a list of dicts, then one `pd.DataFrame(...)` |

## Hidden assumptions worth noting (not errors, but should be documented)
- "Total exports" covers only the 14 economies in the file, not world trade.
- Values are nominal USD, so growth mixes price and volume effects.
- The tariff average is a simple average across years **and** product groups.

## Reconciliation
Total 2023 exports from the fixed `total_exports` (12,269,499 USD m) match an Excel pivot of `trade_summary.csv`. Region totals x 1,000 reconcile to the same figure (automated in `test_region_totals_reconcile_with_total`). Top 5 matches Lab 09's `check_answer.py`.

## AI-assisted debugging (typical experience)
Given the failing `test_growth_rate` output, assistants reliably identify the wrong denominator. For `total_exports` they usually spot mean vs sum. Some suggested changing the test for `average_tariff` to expect 10.0: **wrong**, the test was right. This shows why the human decides.

## Lessons learned
- Eight of the nine errors ran without any error message.
- Comparing docstrings with code found most errors before running anything.
- Small fixtures with hand-calculated answers turn "looks plausible" into "proven".
