# Lab 11: Review and Improve an AI-Generated Solution Containing Deliberate Errors

**Duration:** 75 minutes
**Type:** Code review, testing and debugging exercise

## Objectives
- Review AI-generated code systematically
- Identify mistakes and hidden assumptions
- Write pytest tests that expose errors, using small data with known answers
- Debug with AI assistance without handing over your judgement
- Reconcile results to ensure analytical accuracy

## Scenario
A colleague used an AI assistant to write `export_summary.py`, and plans to use its numbers in a briefing tomorrow. It runs (mostly) and the output looks plausible. It contains **at least nine** deliberate errors: wrong calculations, wrong assumptions, wrong units, an outdated API and a fragile file path. Find them, prove them with tests, and fix them.

## Setup
```bash
pip install pytest
```
(already in `requirements.txt`). Run everything from the **repository root**.

## Steps
1. **Read before you run (15 min).** Read `export_summary.py` line by line with the evaluation checklist from Module 09. For each function compare the **docstring** (what it promises) with the **code** (what it does). Record suspected problems in `review.md`.
2. **Run it.**
   ```bash
   python labs/11-validating-and-testing-ai-code/export_summary.py
   ```
   Then run it from inside the lab folder. What happens, and why?
3. **Run the starter tests.**
   ```bash
   pytest labs/11-validating-and-testing-ai-code -v
   ```
   Two tests are provided. Read the failure messages: expected vs actual.
4. **Write tests (25 min).** In `test_export_summary.py`, add at least one test per remaining function. Work out the expected values **by hand** from the fixtures before you write the assertion. Include edge cases, for example: a missing tariff value, growth from zero, a year with no data.
5. **Debug with AI assistance.** For one failing test, paste the test, the failure output and the function into your AI assistant and ask: *"Explain why this test fails and suggest the smallest fix. Do not change the test."* Decide whether its explanation is right before you accept it.
6. **Fix** each error in `export_summary.py` until all tests pass. Do not change a test to make it pass unless the test itself is wrong, and note it in `review.md` if so.
7. **Reconcile.** Check one real result independently, for example total 2023 exports with an Excel pivot table of `data/trade_summary.csv`, or top 5 exporters against `labs/09-introduction-to-generative-ai/check_answer.py`.
8. **Record** each error in `review.md`: where, what was wrong, how you found it (reading, running, testing, reconciling), and the fix.

## Acceptance criteria
- `pytest labs/11-validating-and-testing-ai-code -v` passes with at least 10 tests
- The script runs from any folder and prints a correct report
- `review.md` lists every error found, how it was found and how it was fixed

## Hints
- Compare every docstring with its code: "percentage", "USD billions", "largest", "ignoring missing values", "exports minus imports".
- `pd.isna(x)` or `math.isnan(x)` test for missing values; `pytest.approx` compares floats.
- `DataFrame.append` was removed in pandas 2.0.
- Paths: `Path(__file__).resolve()` gives the script's own location.
