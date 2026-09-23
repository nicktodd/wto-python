# Lab 09: Generate a Python Solution with an AI Assistant and Evaluate It

**Duration:** 45 minutes
**Type:** Guided exercise using your preferred AI assistant

## Objectives
- Use a Generative AI (GenAI) coding assistant to produce a working Python script
- Compare the effect of a vague prompt and a specific prompt
- Evaluate AI-generated code against a checklist and a known correct answer
- Detect hallucinations by checking claims against official sources

## Setup
- Open the repository root in VS Code (Visual Studio Code) and select the `.venv` interpreter.
- Open the chat panel of **your preferred AI assistant** (for example GitHub Copilot Chat, ChatGPT, Claude or Microsoft Copilot). Use only an assistant your organisation has approved.
- Open `labs/09-introduction-to-generative-ai/evaluation.md`: you will record your results there.
- Only share the course's illustrative data with the assistant. Do not paste anything confidential.

## The task you will give the AI
> Read `data/trade_summary.csv` and print the five largest exporters in 2023 (total exports across all product groups) and each one's share of total 2023 exports, as a percentage to one decimal place.

## Steps
1. **Vague prompt.** Ask your assistant: `Write Python to find the top exporters.` Save the code as `labs/09-introduction-to-generative-ai/attempt1.py` and try to run it. In `evaluation.md`, note what the assistant had to assume.
2. **Specific prompt.** Write your own specific prompt that states the file path, the column names (open the CSV to find them), the year, what "largest" means and the output format. Save the result as `attempt2.py` and run it:
   ```bash
   python labs/09-introduction-to-generative-ai/attempt2.py
   ```
   Tip: file paths in the generated code are relative to the folder you run from.
3. **Verify.** Run the checker and compare the numbers:
   ```bash
   python labs/09-introduction-to-generative-ai/check_answer.py
   ```
4. **Evaluate.** Complete the evaluation table in `evaluation.md` using the checklist in `demos/09-introduction-to-generative-ai/evaluation-checklist.md`.
5. **Ask for an explanation.** Ask the assistant to explain its code line by line. Did the explanation match what the code actually does?
6. **Hallucination hunt.** Ask the assistant two factual questions and check each against an official source. Suggestions:
   - "What is the World Bank indicator code for exports of goods and services as a percentage of GDP?" (check: https://data.worldbank.org)
   - "What parameters does the WTO Timeseries API take for merchandise trade values?" (check: https://apiportal.wto.org)
   - "Which pandas function combines two DataFrames on a common column?" (check: https://pandas.pydata.org/docs)
7. **Reflect.** Answer the three reflection questions.

## Acceptance criteria
- `attempt2.py` runs and its numbers match `check_answer.py`, or you have explained exactly why they differ
- The evaluation table is complete, with evidence for each row
- At least two claims have been fact-checked against official sources

## Stretch
Ask the assistant to add a bar chart of the top five with matplotlib, saved as a PNG. Check that the chart's values match the printed ones.
