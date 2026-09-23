# Demo: Module 11: Validating and Testing AI-Generated Code

**Duration:** 12 minutes
**Prerequisite:** VS Code open at `demos/11-validating-and-testing-ai-code/`, a terminal in that folder with `.venv` active, and `pytest` installed (`pip install pytest`, already in `requirements.txt`). Your preferred AI assistant open.

## Part 1: Review before running (3 min)
Open `ai_generated_growth.py`. Read `yoy_growth` aloud. Ask: "Does this look right?" Most people say yes.
Run it:
```bash
python ai_generated_growth.py
```
Scroll to the row where the reporter changes. The first year of the second reporter has a growth value when it should be blank: `pct_change()` compared it with the **previous reporter's** last year.

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
