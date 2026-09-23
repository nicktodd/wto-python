# Demo: Module 12: Responsible and Secure Use of AI

**Duration:** 10 minutes
**Prerequisite:** VS Code open at `demos/12-responsible-and-secure-ai/`. Have your organisation's AI policy (or its intranet page) to hand if one exists. Open `responsible-ai-checklist.md`.

## Part 1: What leaves the building? (3 min)
Ask the room: "When you paste something into an AI chat, where does it go?" Discuss:
- Enterprise vs consumer tools: data retention, training on your data, where the data is stored
- Why **approved** tools matter even when the content seems harmless
- Data classification: public statistics vs internal drafts vs personal data

## Part 2: Spot the vulnerability (5 min)
Open `insecure_patterns.py`. **Do not run it.** For each numbered block, ask the class what is wrong before revealing:
1. Hard-coded secret: it ends up in git history forever. Show the environment-variable fix.
2. `verify=False`: disables protection against interception. AI often suggests it to "fix" certificate errors.
3. SQL built with an f-string: injection. Show the parameterised fix.
4. Personal data in logs: logs are copied, shared and kept for a long time.
5. Confidential text posted to an unapproved external AI service.
6. `eval` on input: arbitrary code execution.

Optional live moment: ask your AI assistant *"My requests call fails with an SSL certificate error. How do I fix it?"* and see whether it suggests `verify=False`. Discuss the right fix (install the organisation's certificate bundle, or ask IT).

## Part 3: Human oversight (2 min)
Walk through "When not to rely on AI" on the checklist. "Accountability does not transfer to the tool: if your name is on the briefing, you own every number in it."

## Key message
Use approved tools, share the minimum data, review generated code for security flaws, and keep a human accountable for every output.
