# Lab 02: Process Trade and Economic Data with Python

**Duration:** 45 minutes
**Type:** Notebook code exercise

## Objectives
- Use variables, strings, numbers, lists and dictionaries
- Apply conditional logic and loops to records
- Write small reusable functions and check them with `assert`

## Steps
1. Open `labs/02-python-basics/trade_basics.ipynb` in JupyterLab.
2. Run the first code cell to load eight trade records (a list of dictionaries).
3. Work through Tasks 1 to 5. After each task run the **check** cell: it prints `Task N OK` when your code is correct, or raises an `AssertionError` if not.
   - Task 1: `clean_name()` to fix spacing and capitalisation
   - Task 2: `to_number()` to convert `"14,600"` to `14600.0`
   - Task 3: build a cleaned list of records
   - Task 4: classify each record as surplus or deficit
   - Task 5: build a nested dictionary and calculate export growth
4. Try the stretch tasks if you finish early.

## Acceptance criteria
- All five check cells print `OK`
- *Kernel > Restart Kernel and Run All Cells* completes without errors

## Hints
- `" kenya".strip().title()` returns `"Kenya"`
- `isinstance(value, str)` tells you whether a value is text
- `dict.setdefault(key, {})` returns the inner dictionary, creating it if needed
