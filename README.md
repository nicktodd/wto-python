# Python for Data Extraction and AI-Assisted Development: Lab Exercises

This repository contains the demos, hands-on labs and reference solutions for the three-day
*Python for Data Extraction and AI-Assisted Development* course.

## Prerequisites

- Python 3.10 or later ([python.org](https://www.python.org/downloads/))
- A web browser (for JupyterLab)
- Visual Studio Code (from Module 08), with your organisation's approved AI coding assistant
  (for example GitHub Copilot, ChatGPT, Claude or similar)
- Internet access for Modules 05 and 06 (cached copies of all data are provided if access is blocked)

## Setup

Open a terminal (Command Prompt, PowerShell or Terminal) in the repository folder and run:

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
jupyter lab
```

JupyterLab opens in your browser. Navigate to `labs/` to begin.

## Structure

| Folder | Purpose |
|---|---|
| `data/` | Shared datasets used across modules |
| `demos/<module>/` | Instructor demonstration material (demo guides, notebooks) |
| `labs/<module>/` | Your exercises: a `README.md` with instructions plus starter notebooks/scripts |
| `solutions/<module>/` | Reference solutions. Try the lab first before looking! |

### About the data

The files in `data/` are **illustrative**: they are shaped like WTO and UN Comtrade merchandise
trade statistics but the figures are synthetic and must not be quoted as official statistics.
`trade_raw_2019_2023.csv` deliberately contains quality problems (inconsistent names, missing
values, duplicates, mixed date formats) for the cleaning exercises. Modules 05 and 06 use **real**
public data from the World Bank and published statistics web pages.

## Modules

### Python Fundamentals
- [Module 01: Introduction to Python and Data Workflows](labs/01-introduction/README.md)
- [Module 02: Python Basics](labs/02-python-basics/README.md)
- [Module 03: Working with Files](labs/03-working-with-files/README.md)
- [Module 04: Introduction to pandas](labs/04-introduction-to-pandas/README.md)

### Data Extraction and Preparation
- [Module 05: Acquiring Data from External Sources](labs/05-acquiring-data-from-apis/README.md)
- [Module 06: Collecting Data from Web Sources](labs/06-collecting-data-from-web-sources/README.md)
- [Module 07: Data Cleaning and Transformation](labs/07-data-cleaning-and-transformation/README.md)
- [Module 08: Building Reusable Data Pipelines](labs/08-building-reusable-data-pipelines/README.md)

### AI-Assisted Python Development
- [Module 09: Introduction to Generative AI for Developers](labs/09-introduction-to-generative-ai/README.md)
- [Module 10: Prompting Techniques for Python Development](labs/10-prompting-techniques/README.md)
- [Module 11: Validating and Testing AI-Generated Code](labs/11-validating-and-testing-ai-code/README.md)
- [Module 12: Responsible and Secure Use of AI](labs/12-responsible-and-secure-ai/README.md)

### Capstone (optional)
- [Capstone: Build an AI-Assisted Data Extraction Solution](labs/13-capstone/README.md)
