# Lab 12: Assess AI-Generated Code Against Security, Privacy and Governance Requirements

**Duration:** 45 minutes
**Type:** Review and assessment exercise (individual, then compare in pairs)

## Objectives
- Identify security risks in AI-generated code
- Recognise privacy issues when code handles personal or sensitive information
- Apply governance principles and organisational policy to AI-assisted work
- Decide where human oversight is essential, and when not to rely on AI

## Scenario
A colleague asked an AI assistant to automate a weekly tariff briefing. The generated `briefing_tool.py` fetches tariff data, looks up country codes, sends everything to a free online AI summarisation service, and emails the result to every delegation contact. Your manager asks: *"Can we switch this on next Monday?"*

**Do not run `briefing_tool.py`.** All hosts, keys and people in it are fictitious; `contacts_sample.csv` contains made-up placeholder contacts.

## Steps
1. **Read** `briefing_tool.py` from top to bottom, including the prompt in the docstring.
2. Using `demos/12-responsible-and-secure-ai/responsible-ai-checklist.md`, fill in `assessment.md`:
   - **Security:** at least six issues (think: secrets, TLS, timeouts, SQL, deserialisation, `eval`, dependencies)
   - **Privacy:** at least three issues (think: what personal data goes where, logs, data minimisation)
   - **Governance:** at least three issues (think: approved tools, automatic "official" communication, record-keeping, review)
3. **Human oversight:** answer the questions in section 4 of `assessment.md`.
4. **Recommend:** approve, approve with changes, or reject and redesign.
5. **Improve the prompt:** rewrite the original prompt to state security, privacy and review requirements up front.
6. **Pair up** and compare findings. Did your partner find anything you missed?
7. **Optional:** ask your AI assistant to review `briefing_tool.py` for security and privacy issues. Compare its list with yours. What did it miss, and what did it add?

## Acceptance criteria
- At least 12 findings across security, privacy and governance, each with a severity and a fix
- A clear recommendation with reasons
- A rewritten prompt that would prevent the main problems

## Stretch
Sketch (in comments or pseudo-code) a redesigned workflow: local processing only, no personal data in the AI step, a draft saved for human review, and sending done by a person.
