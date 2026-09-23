# Reference card: responsible and secure use of AI assistants

## Before you prompt: data
- [ ] Is this tool **approved** by my organisation for this kind of work?
- [ ] What is the **classification** of the data I am about to share (public, internal, confidential, strictly confidential)?
- [ ] Am I sharing **personal data** (names, emails, IDs of delegates, staff or members of the public)? If so: don't.
- [ ] Could I use **column names and made-up sample rows** instead of real data?
- [ ] Is anything in the prompt **unpublished** (draft reports, negotiating positions, embargoed statistics)?

## After you get code: security
- [ ] No secrets in code, logs, URLs or notebooks; keys come from environment variables or a secrets store
- [ ] HTTPS certificate checks left **on** (no `verify=False`); timeouts set
- [ ] No `eval`/`exec` on input; no `pickle.load` of untrusted files
- [ ] Parameterised SQL (`?` placeholders), never string-built queries
- [ ] Packages exist, are well known and are spelled correctly (AI can invent package names that attackers then register)
- [ ] No personal data in logs or outputs that do not need it

## Governance
- [ ] AI use recorded (tool, date, purpose, prompt log) where policy requires
- [ ] Code reviewed and tested by a human before use (Module 11)
- [ ] Outputs that inform decisions are traceable to sources
- [ ] Licences of generated code and data sources respected

## Human oversight: when **not** to rely on AI
- Final figures for publication or decisions, without independent verification
- Legal interpretation, negotiating positions, or anything requiring institutional judgement
- Confidential or personal data processing through unapproved tools
- When you cannot explain what the generated code does
- When the cost of a subtle error is high and you have no way to check the result
