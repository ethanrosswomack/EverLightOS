# EverLight APM Assistant

**Goal:** Streamline preventive maintenance (PM) documentation, reduce typing and context switching, and generate standardized logs suitable for future automation and AWS integration.

> Local-first. Policy-safe. Easy to port to AWS when approved.

## Features
- 🔢 Structured inputs → paste-ready text for APM
- 📁 CSV + JSON logs for personal metrics and future automation
- 🧠 JSON Schema for validation
- 🧪 Tests and examples
- ☁️ `aws/blueprints/` with CDK/IaC stubs for a future serverless API

## Quick Start

```bash
# (Optional) create & activate venv first
python -m venv .venv && source .venv/bin/activate   # Linux/macOS
# or: .venv\Scripts\activate                      # Windows PowerShell

pip install -e .

# Run CLI
apm-assistant --help
apm-assistant new --site TPA4 --area "3rd floor" --shift "N2" --tech "Ethan" --mod "Jessi"
apm-assistant add --equip "Charger-36" --comp "filter" --action "cleaned" --result "pass" --mins 5
apm-assistant render
```

Outputs are written into `./runs/<timestamp>/`:
- `apm_paste.txt` — paste into APM
- `pm_log.csv` — structured log
- `pm_log.json` — data for LLMs or APIs

## Repository Structure

```
everlight-apm-assistant/
├─ src/everlight_apm_assistant/
│  ├─ __init__.py
│  ├─ cli.py
│  ├─ core.py
│  ├─ schema.py
│  └─ storage.py
├─ examples/
│  └─ sample_session.json
├─ tests/
│  ├─ test_core.py
│  └─ test_cli.py
├─ docs/
│  └─ DESIGN.md
├─ aws/
│  └─ blueprints/
│     ├─ README.md
│     └─ cdk_skeleton.md
├─ runs/            # gitignored; holds local outputs
├─ .github/workflows/ci.yml
├─ .gitignore
├─ LICENSE
├─ pyproject.toml
├─ setup.cfg
└─ README.md
```

## Policy-Safe Usage

- Use locally to generate paste blocks; **do not** automate login or submission to internal systems without written approval.
- Keep logs free of sensitive data unless you have permission and secure storage.
- When ready, use `aws/blueprints/` to port to a serverless API with formal approvals.

## Roadmap
- Snippets/presets for common equipment
- OneNote export helpers
- Optional GUI (web or TUI)
- AWS port (API Gateway + Lambda + DynamoDB) with SSO
