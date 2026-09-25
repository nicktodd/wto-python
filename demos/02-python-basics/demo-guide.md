# Demo: Module 02: Python Basics

**Duration:** run alongside the slides (about 2 to 3 minutes per section)
**Prerequisite:** JupyterLab open at `demos/02-python-basics/python_basics.ipynb`.

The notebook has one `##` section per code slide, in slide order. Run each cell as you reach its slide so delegates see the output appear live; the slide shows the same code and output for reference.

## Section 1: Values and variables
- Run *print and comments*, *Variables*, *Data types*.
- Change a value and re-run to show that variables hold the **latest** assignment.
- Ask the room to predict each `type()` before you run it.

## Section 2: Numbers
- *Arithmetic*: ask what `10 / 3` and `10 // 3` will print before running.
- *Calculating with variables*: point out the step-by-step names (`change`, `growth`).

## Section 3: Strings
- *String methods*: `repr()` reveals the hidden spaces that break matching.
- *A conversion error* raises a `ValueError` **on purpose**. Read the last line of the error aloud, then show the fix in *Converting types*.

## Section 4: Collections
- *Tuples* ends with a `TypeError` **on purpose**, to show that tuples cannot change.
- *Lists of dictionaries*: "This is a table. pandas in Module 04 gives us a much more powerful version."

## Section 5: Decisions and loops
- *if elif else*: change `imports` to 5000 and re-run to show the other branch.
- *Accumulating a total*: the running total print shows exactly what the loop does each time round.
- *Building a new list* and *List comprehensions* give the same result two ways.

## Section 6: Functions
- *return versus print*: `a` is `None`. "If you want to use the result, return it."
- *Putting it together* previews Part F of the lab.

## Key message
Everything in data analysis is built from these few building blocks: values, collections, decisions, repetition and reusable functions.
