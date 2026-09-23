# Assessment: briefing_tool.py (instructor answer key)

## 1. Security

| # | Where | Issue | Severity | Fix |
|---|---|---|---|---|
| S1 | `STATS_API_KEY`, `SMTP_PASSWORD` | Secrets hard-coded in source; they end up in git history, backups and AI chat logs | High | Environment variables or the organisation's secrets store; rotate both credentials now |
| S2 | `fetch_tariffs` | API key placed in the URL **and** the URL logged at DEBUG, so the key is written to `briefing.log` | High | Send the key in a header; never log URLs containing credentials |
| S3 | `fetch_tariffs` | `verify=False` disables TLS (Transport Layer Security) certificate checks, allowing interception | High | Remove it; install the organisation's CA (Certificate Authority) bundle if needed |
| S4 | `fetch_tariffs`, `summarise` | No timeouts; no status or error checks | Medium | `timeout=30`, `raise_for_status()`, handle `RequestException` |
| S5 | `lookup_iso3` | SQL built with an f-string from user input: SQL injection | High | Parameterised query `WHERE name = ?` |
| S6 | `apply_user_filter` | `eval()` on typed input: arbitrary code execution | High | Offer fixed filter options, or parse a restricted rule format |
| S7 | `load_previous` | `pickle.load` can execute code from a tampered file | Medium | Store the previous week as CSV or Parquet |
| S8 | `import wto_tariff_tools` | Unknown package suggested by the AI; may not exist, or may be a malicious look-alike registered by an attacker ("slopsquatting") | High | Remove; only install well-known packages from approved sources, pin versions |
| S9 | `email_everyone` | Unencrypted SMTP (Simple Mail Transfer Protocol) on port 25 with login | Medium | Use the organisation's mail service with TLS, or do not send automatically |

## 2. Privacy and data protection

| # | Where | Issue | Severity | Fix |
|---|---|---|---|---|
| P1 | `summarise` | Delegates' names, emails and phone numbers sent to an unapproved external AI service: an unauthorised disclosure of personal data | High | Never send personal data to the AI step; recipients are not needed to summarise tariffs |
| P2 | `load_contacts`, `email_everyone` | Full contact records (including phone numbers) written to a log file | High | Log counts or IDs only; minimise log retention |
| P3 | `summarise` | Unpublished comparison data sent to a third party with unknown retention and training terms | High | Use an approved enterprise tool, or summarise locally |
| P4 | Overall | Data minimisation: phone numbers are loaded but never needed | Low | Load only the columns required |

## 3. Governance and organisational policy

| # | Issue | Severity | Action |
|---|---|---|---|
| G1 | "free-ai-summary" is not an approved tool; the AI use is not recorded | High | Use only approved tools; record the tool, purpose and prompt log |
| G2 | Emails are labelled "official" and sent automatically, with AI-written content nobody has read | High | Human review and sign-off before any communication; a person sends it |
| G3 | No tests, validation or source attribution in the briefing; figures cannot be traced | Medium | Validate data (Module 07/11); cite the data source and date in the briefing |
| G4 | Scheduled mass email to external delegations may breach communication policy | High | Check with the communications or data protection office |

## 4. Human oversight and accountability
- **Review point:** none. The summary goes straight from an external AI service to delegations.
- **Accountability:** the person who deployed the tool and the sending unit remain accountable; "the AI wrote it" is not a defence.
- **Do not delegate to AI:** the decision to send official communications; interpreting tariff changes for delegations; any processing of personal data through unapproved tools.

## 5. Recommendation
**Reject and redesign.** The tool leaks credentials and personal data, has several critical vulnerabilities, and removes human review from official communications. See `briefing_draft.py` for a safer design: local processing, no personal data, and a draft saved for human review.

## 6. Improved prompt
```
Write a Python script for an internal analyst that:
- reads data/tariffs_mfn.csv (public-style tariff data; no personal data)
- compares the latest two years for each country and product group
- writes a Markdown DRAFT briefing to output/ for a human to review; it must
  not send email or call any external service
- cites the data source and the date the script was run
Security requirements: no secrets in code; if any credential is ever needed,
read it from an environment variable; no eval/exec/pickle; parameterised SQL
only; use only pandas and the standard library.
Explain any assumptions in comments.
```
