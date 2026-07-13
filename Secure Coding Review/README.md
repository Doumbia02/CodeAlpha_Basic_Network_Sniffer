# Secure Coding Review — SecureNotes (Flask/Python)

A hands-on security audit of a small Flask web application: static analysis + manual
code review, 11 documented vulnerabilities mapped to CWE, and a fully remediated
version of the code.

## Overview

| | |
|---|---|
| **Application audited** | SecureNotes — sample Flask/Python app (login, notes, file download, outbound HTTP) |
| **Language / framework** | Python 3.12, Flask |
| **Review methods** | Static analysis ([Bandit](https://bandit.readthedocs.io/) v1.9.4) + manual line-by-line inspection |
| **Findings** | 11 (3 Critical, 6 High, 2 Medium) |
| **Full report** | [`reports/SECURE_CODING_REVIEW.docx`](reports/SECURE_CODING_REVIEW.docx) |

## Repository structure

```
.
├── src/
│   ├── vulnerable_app.py     # audited app — intentionally vulnerable, for reference
│   └── secure_app.py         # remediated version — fixes every finding below
├── reports/
│   ├── SECURE_CODING_REVIEW.docx   # full write-up: methodology, findings, remediation
│   ├── bandit_report.txt           # Bandit output — before remediation
│   └── bandit_report_fixed.txt     # Bandit output — after remediation
├── .github/workflows/bandit.yml    # CI: runs Bandit on every push/PR
└── requirements.txt
```

## Findings summary

| # | Finding | CWE | Severity |
|---|---|---|---|
| 1 | SQL injection via string-formatted query | CWE-89 | 🔴 Critical |
| 2 | Weak password hashing (unsalted MD5) | CWE-327 | 🟠 High |
| 3 | Predictable session token (insecure PRNG) | CWE-330 | 🟠 High |
| 4 | Hardcoded secret key in source | CWE-798 | 🟡 Medium |
| 5 | Reflected XSS | CWE-79 | 🟠 High |
| 6 | OS command injection (`shell=True`) | CWE-78 | 🔴 Critical |
| 7 | Path traversal / arbitrary file read | CWE-22 | 🟠 High |
| 8 | Insecure deserialization (`pickle.loads`) | CWE-502 | 🔴 Critical |
| 9 | Server-Side Request Forgery (SSRF) | CWE-918 | 🟠 High |
| 10 | Broken access control (IDOR) | CWE-639 | 🟠 High |
| 11 | Debug mode + bind-all in entrypoint | CWE-489 / CWE-605 | 🟡 Medium |

Full details — issue, impact, and remediation for each — are in the report.

## Methodology

1. **Static analysis** — [Bandit](https://bandit.readthedocs.io/) scanned the source for
   known-insecure patterns (weak crypto, `shell=True`, unsafe deserialization, etc.).
2. **Manual review** — every route handler was inspected by hand, tracing user input
   (form fields, query strings, cookies, uploaded files, URLs) to its sink (SQL query,
   shell command, filesystem path, deserializer, outbound request). This step caught
   issues Bandit's pattern-matching missed: reflected XSS, path traversal, and IDOR all
   depend on business logic a static tool can't reason about.

## Reproducing the scan

```bash
pip install -r requirements.txt
bandit -r src/vulnerable_app.py -f txt   # before: 3 High / 4 Medium / 4 Low
bandit -r src/secure_app.py -f txt       # after:  0 High / 0 Medium
```

## Key fixes applied (`secure_app.py`)

- Parameterized SQL queries everywhere (no string-built queries)
- Passwords hashed with `werkzeug.security` (salted PBKDF2) instead of raw MD5
- Session tokens generated with `secrets.token_urlsafe`, cookies set `HttpOnly` /
  `Secure` / `SameSite`
- Secret key loaded from an environment variable, not committed to source
- HTML output rendered through Jinja2's auto-escaping instead of string concatenation
- No `shell=True`; subprocess arguments passed as a list with validated input
- File paths resolved and checked against an allow-listed root directory
- `pickle` replaced with JSON + explicit schema validation
- Outbound requests restricted to an allow-list of hosts, with a timeout
- Per-object ownership/authorization checks added to the notes endpoint
- Debug mode off, bound to loopback; intended to run behind a real WSGI server

## Disclaimer

`src/vulnerable_app.py` is intentionally insecure and included **for review/teaching
purposes only**. Do not deploy it, and do not reuse its patterns.

## License

[MIT](LICENSE)
