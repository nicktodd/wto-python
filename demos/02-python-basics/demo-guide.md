# Demo: Module 02: Python Basics

**Duration:** 12 minutes (spread through the module; run each section after the matching slides)
**Prerequisite:** JupyterLab open at `demos/02-python-basics/python_basics.ipynb`.

## Part 1: Variables, types and strings (3 min)
Run the first two code cells.
- Point out that Python works out the type for you: `str`, `int`, `float`, `bool`.
- Show `strip()` and `title()` fixing a messy country name: "This is exactly the kind of clean-up we automate on Day 2."
- Show the f-string format `:,.1f` producing a thousands separator.

## Part 2: Numbers and conversion (2 min)
Run the numbers cell. Ask: "What happens if you do `float("1,234.5")` without the replace?" Try it live to show the `ValueError`, then undo.

## Part 3: Lists and dictionaries (3 min)
- Lists: an ordered collection; index from 0; `-1` is the last item.
- Dictionaries: a record with named fields, like one row of a spreadsheet.
- "A list of dictionaries is a table. Hold that thought for pandas in Module 04."

## Part 4: Conditions, loops and functions (4 min)
- Conditions: change `imports` to 5000 and re-run to show the other branch.
- Loops: accumulate a total; then the list comprehension doing a filter.
- Functions: `growth_rate` guards against division by zero. "Name it, test it, reuse it."

## Key message
Everything in data analysis is built from these few building blocks: values, collections, decisions, repetition and reusable functions.
