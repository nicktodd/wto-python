# Demo: Module 01: Introduction to Python and Data Workflows

**Duration:** 10 minutes
**Prerequisite:** Repository cloned, virtual environment created, `jupyter lab` running from the repository root.

## Part 1: A tour of JupyterLab (4 min)

1. Show the file browser on the left. Open `demos/01-introduction/first_look.ipynb`.
2. Point out the two cell types: **Markdown** (notes) and **Code**.
3. Run the first code cell with **Shift+Enter**. Point at the `[1]` execution counter.

Narration: "A notebook is a lab book. Your code, your results and your reasoning sit side by side,
so a colleague can follow what you did and re-run it."

## Part 2: First look at trade data (4 min)

Run the remaining cells in order:

- `import pandas as pd`: "pandas is the spreadsheet engine of Python. We study it properly in Module 04."
- `df.head()`: compare with opening a CSV in Excel.
- `df.shape`, `df.columns`: "How big is it? What is in it?"
- The group-by cell: "One line gives total exports by region. In Excel this is a pivot table."

Do **not** explain the pandas syntax in detail; the goal is motivation, not mastery.

## Part 3: From data to questions (2 min)

Ask the room: "Looking at these columns, what questions could we answer?" Capture 3-4 on the
whiteboard, for example:

- Which region's exports recovered fastest after 2020?
- What share of Kenya's exports are agricultural products?
- Which countries run a trade surplus in manufactures?

## Key message
Python turns repeatable data questions into repeatable code: analysis you write once can be re-run on next year's data in seconds.
