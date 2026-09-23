# Reference card: prompt patterns for Python development

## The CRAFT checklist
| Letter | Include | Example |
|---|---|---|
| **C**ontext | Business purpose, data, environment | "For a WTO briefing on tariffs; Python 3.12, pandas, requests" |
| **R**ole | Who the assistant should act as | "Act as a senior Python data engineer" |
| **A**sk | One clear task | "Write a function that extracts..." |
| **F**ormat | Shape of the answer | "A single .py file with docstrings; explain in 5 bullets" |
| **T**hresholds | Constraints and quality bars | "Timeout 30s; no API keys in code; handle missing values" |

## Useful follow-up prompts
- "What assumptions did you make? List them."
- "Explain this line by line for a beginner."
- "What could go wrong with this code? How would I test it?"
- "Refactor this into functions with docstrings and type hints."
- "Add logging and error handling for network failures."
- "Write pytest tests for this function, including edge cases."
- "Show me the official documentation for the functions you used."

## Iterate: do not start over
1. Start with a working minimum.
2. Add one requirement per prompt.
3. Run and check after every change.
4. Paste the actual error message back to the assistant when something fails.
5. Keep a prompt log of what worked.

## Give the data, not the whole dataset
Paste the **column names and 3 to 5 sample rows** (of non-sensitive data), not the entire file.
