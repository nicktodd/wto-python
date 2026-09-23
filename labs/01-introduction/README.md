# Lab 01: Explore a Trade Dataset

**Duration:** 30 minutes
**Type:** Notebook exploration

## Objectives
- Confirm your Python and JupyterLab environment works
- Load a trade dataset and describe its structure
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

## Steps

1. In JupyterLab open `labs/01-introduction/explore_trade.ipynb`.
2. Run the environment check cell (Shift+Enter). You should see Python 3.10+ and a pandas version.
3. Load `data/trade_summary.csv` and display the first 10 rows.
4. Describe the dataset: number of rows and columns, years, reporters and product groups.
5. Run the yearly summary cell and explain the 2020 figures in a Markdown cell.
6. Complete the analytical questions table (five questions).
7. List two questions the data **cannot** answer and what extra data you would need.

## About the data

`trade_summary.csv` (CSV: Comma-Separated Values) holds annual exports and imports in USD millions
for 14 economies, 2019-2023, split into four product groups. It is illustrative data shaped like
WTO statistics; do not quote the figures.

## Acceptance criteria
- Every code cell runs without errors
- The dataset description is complete
- Five analytical questions, each with the columns it needs
- Two gaps identified

## Stretch
Open `data/tariffs_mfn.csv` in the same way. What questions become possible when you combine it with the trade data?
