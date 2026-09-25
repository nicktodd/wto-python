# Lab 02: Process Trade and Economic Data with Python

**Duration:** 60 to 75 minutes
**Type:** Notebook code exercise, built up in small steps

## Objectives
- Create variables and do calculations
- Clean text and convert text to numbers
- Use lists and `for` loops
- Write small functions that return values
- Read and update dictionaries
- Combine all of the above to clean a list of trade records

## How this lab works
The lab is split into short steps. Each step introduces **one** idea, shows you what to type (look back at the matching slide or the demo notebook `demos/02-python-basics/python_basics.ipynb`), and has a **check** cell that prints `OK` when your code is right.

Later steps reuse earlier ones, so work in order.

| Part | You will practise | Steps |
|---|---|---|
| A | Variables, types, calculations, f-strings | A1 to A4 |
| B | Cleaning text: `strip()`, `title()`, converting `"14,600"` to a number | B1 to B4 |
| C | Lists and loops: print, clean, build a new list, add up values | C1 to C5 |
| D | Functions: `clean_name()`, `to_number()`, `classify_balance()` | D1 to D4 |
| E | Dictionaries: read, update and add keys in a trade record | E1 to E3 |
| F | Putting it together: clean eight trade records and report on them | F1 to F4 |

## Steps
1. Open `labs/02-python-basics/trade_basics.ipynb` in JupyterLab.
2. Work through Parts A to F. In each code cell replace `...` or `# TODO` with your code, run it, then run the check cell below it.
3. If you finish early, try the stretch step at the end.

## Tips
- If a check fails, read the **last line** of the error first.
- `NameError` usually means an earlier cell has not been run: use *Run > Run All Above Selected Cell*.
- Indentation matters: code inside a loop or function is indented by 4 spaces.

## Acceptance criteria
- Every check cell prints `OK`
- *Kernel > Restart Kernel and Run All Cells* completes without errors
