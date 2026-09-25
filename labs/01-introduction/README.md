# Lab 01: Explore a Trade Dataset

**Duration:** 30 minutes
**Type:** Guided notebook exploration: **no coding required**

## Objectives
- Confirm your Python and JupyterLab environment works
- Run Python code in a Jupyter notebook and read its output
- Describe the structure and coverage of a trade dataset
- Turn a dataset into a set of analytical questions

## Setup

If you have not already done so, from the repository root run:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

On macOS/Linux activate with `source .venv/bin/activate`.

## How this lab works
Every code cell in the notebook is **already written for you**. You will:
1. read the short explanation above each cell,
2. run the cell with **Shift+Enter**,
3. look at the output and answer the question in the *Your answer* cell (double-click to edit).

In two steps you make a tiny change (a number, a country name) and run the cell again. You will learn to write this kind of code yourself in Modules 02 to 04.

## Steps
1. In JupyterLab open `labs/01-introduction/explore_trade.ipynb`.
2. Work through Steps 1 to 8: check your environment, load the data, see its size and coverage, and look at trade by year, by country and by region.
3. Step 9: write five analytical questions the data could answer.
4. Step 10: list two questions it **cannot** answer and the extra data you would need.

## About the data
`trade_summary.csv` (CSV: Comma-Separated Values) holds annual exports and imports in USD millions
for 14 economies, 2019-2023, split into four product groups. It is illustrative data shaped like
WTO statistics; do not quote the figures.

## Acceptance criteria
- Every code cell has been run without errors
- Every *Your answer* cell is filled in
- Five analytical questions, each with the columns it needs, and two data gaps

Example answers are in `solutions/01-introduction/explore_trade.ipynb`.
