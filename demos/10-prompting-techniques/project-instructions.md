# Project instructions for AI assistants (example)

Many assistants can read standing instructions so you do not repeat context in every prompt:
- GitHub Copilot: `.github/copilot-instructions.md`
- Claude Code: `CLAUDE.md`
- ChatGPT: custom instructions or a project
- Others: paste this at the start of a chat

---

This repository contains Python data extraction scripts for trade and economic analysis.

- Python 3.10+, pandas, requests, BeautifulSoup. Do not add other dependencies without asking.
- Data files live in `data/`. Never modify files in `data/`; write outputs to an `output/` folder.
- Country identifiers: use ISO3 codes (for example `KEN`), never free-text names, for joins.
- Monetary values are USD millions unless the column name says otherwise.
- Every HTTP request must have a timeout and handle `requests.RequestException`.
- Never put API keys or passwords in code; read them from environment variables.
- Use the `logging` module, not `print`, in scripts.
- Write functions with docstrings; keep functions small and testable with pytest.
- Explain any assumption about data definitions in a comment.
