# Soldier Knowledge Network

Soldier Knowledge Network (SKN) is an independent, unofficial resource directory and professional-development platform for the Army workforce and community.

## Mission

**Make trusted Army information easier to find, understand, and use.**

## Current release

- Version: `0.2.0`
- Stage: Public Alpha
- Hosting: Cloudflare Pages
- Architecture: Static HTML, CSS, JavaScript, and JSON
- Accounts/database: None

## Core capabilities

- Task-based search with Army acronyms, common terms, and legacy system names
- Audience filters for Soldiers, Guard, Reserve, Civilians, contractors, families, retirees, and veterans
- Frequently used resources
- Browser-based favorites with no account
- Clear source, owner, access, network, domain, status, and verification information
- Structured broken-link, correction, and resource-request forms
- Automated JSON validation and scheduled public-link checks
- Public update log and project governance standards

## Repository structure

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── assets/icons/
├── data/
│   ├── resources.json
│   ├── site.json
│   └── updates.json
├── docs/
├── pages/
├── scripts/
├── 404.html
├── index.html
├── script.js
└── styles.css
```

## Run locally

A local web server is required because the site loads JSON with `fetch()`.

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Add or edit a resource

Edit `data/resources.json`. Every entry must pass `scripts/validate_data.py`.

```bash
python scripts/validate_data.py
```

Required fields include a unique ID, official owner, source type, audiences, access conditions, network requirement, status, verification date, tasks, keywords, and HTTPS URL.

## Contributing and reporting

- Read [CONTRIBUTING.md](CONTRIBUTING.md).
- Report a public navigation problem through the issue templates.
- Do not submit credentials, PII, CUI, medical records, orders, rosters, internal screenshots, or operational information.

## Disclaimer

SKN is not an official Department of Defense or Department of the Army website. It does not replace official policy, systems of record, authorized support channels, or professional advice. External hyperlinks are provided for navigation and do not constitute endorsement.
