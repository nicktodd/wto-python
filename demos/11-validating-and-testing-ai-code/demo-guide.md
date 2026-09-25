# Demo: Module 11: Validating and Testing AI-Generated Code

**Duration:** 12 minutes
**Prerequisite:** VS Code open at `demos/11-validating-and-testing-ai-code/`, a terminal in that folder with `.venv` active, and `pytest` installed (`pip install pytest`, already in `requirements.txt`). Your preferred AI assistant open.

## Part 1: Spot the problem (4 min)
Open `ai_generated_growth.py` and read `yoy_growth` aloud. Ask: "Does this look right?" Most people say yes.
Run it on a tiny table where we know the answers:
```bash
python spot_the_problem.py
```
- Ask the room to check each growth value. Ghana 2023 (-2.9%) and Kenya 2023 (-6.8%) are right.
- Kenya 2022 shows **-52.7%**. It is Kenya's first year, so it should be blank (NaN), like Ghana 2022.
- Ask: "Where did -52.7% come from?" It is Kenya 2022 (7,950) compared with **Ghana 2023** (16,800).
- Explain: `pct_change()` compares each **row** with the row above. It knows nothing about reporters, so the first row of each new country is compared with the last row of the previous one.
- Show the fix and its output:
```bash
python spot_the_problem.py --fixed
```
- "On our full dataset of 14 reporters there would be 13 invented growth rates, with no error and no warning."

## Part 2: A test makes the bug undeniable (4 min)
Open `test_ai_generated_growth.py`. Explain the fixture: "a tiny table where we know the answers by hand."
```bash
pytest -v
```
`test_first_year_has_no_growth` fails; the other two pass. Point out that `test_growth_values` passes even though the function is wrong: "one test is never enough." Read the failure output together: expected vs actual.

## Part 3: Debug with AI assistance (3 min)
Paste the failing test output and the function into your AI assistant with:
```
This pytest test fails. Explain why, and suggest the smallest fix.
Do not change the test.
```
Apply the fix it suggests (it should be a group-wise calculation):
```python
totals["growth_pct"] = (
    totals.groupby("reporter")["exports_usd_m"]
    .pct_change() * 100).round(1)
```
Run `pytest -v` again: all green. Undo the fix afterwards so the demo is ready for next time (`git checkout ai_generated_growth.py`).

## Part 4: Analytical accuracy (2 min)
"Tests prove the code does what we specified. Reconciliation proves the numbers are right: do totals match a published source or an independent calculation?"

## Key message
Never trust code because it looks right: test it with small data where you know the answer, and reconcile real results against an independent source.
