# Demo: Module 09: Introduction to Generative AI for Developers

**Duration:** 12 minutes
**Prerequisite:** VS Code (Visual Studio Code) open at the repository root, with your organisation's approved AI assistant signed in (GitHub Copilot, ChatGPT, Claude or similar). Have `prompts.md` and `evaluation-checklist.md` from this folder open. Run a quick test prompt beforehand so you know the assistant is available. AI responses vary between runs, so expect different output from these notes.

## Part 0: Day 3 setup check (2 min)
Ask delegates to open VS Code at the repository root, select the `.venv` Python interpreter, and open their AI assistant's chat panel. Confirm each person can get a response. If anyone has no assistant, pair them with someone who does.

## Part 1: Vague vs specific (4 min)
- Paste **Prompt 1**. Narrate: "Look how much it had to guess: which file? which columns? what analysis?"
- Paste **Prompt 2**. Save the output as `scratch_top5.py` in the repo root and run it.
- Compare with the known answer: run `python labs/09-introduction-to-generative-ai/check_answer.py`. "Trust, but verify: we had a way to check."

## Part 2: Explanations (2 min)
Paste **Prompt 3**. "The assistant is a patient tutor. Ask it to explain anything you do not understand, then check the explanation against the documentation."

## Part 3: Hallucinations (4 min)
- Paste **Prompt 4**, then open https://apiportal.wto.org and compare. Point out any invented endpoints or parameters.
- Open `hallucination_examples.py` and walk through the five examples: invented function, invented endpoint, wrong logic that still runs, an invented fact, an outdated API.
- "The dangerous ones are not the errors that crash; they are the ones that run and give a plausible wrong number."

## Key message
AI assistants are fast, fluent and frequently wrong: use them to go faster, but verify everything as if a new colleague wrote it.
