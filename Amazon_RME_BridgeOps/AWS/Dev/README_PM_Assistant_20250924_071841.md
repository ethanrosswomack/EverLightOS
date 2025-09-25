# PM Entry Assistant (Local Tool)

This CLI tool helps you standardize preventive maintenance (PM) notes and quickly create a paste-ready block for internal forms. It does **not** log in or interact with any company systems. It simply reduces typing, standardizes language, and preserves a CSV/JSON log for your records or future automation.

## Files
- `pm_autofill_helper.py` — run this in a terminal: `python pm_autofill_helper.py`
- `apm_paste_*.txt` — formatted text blocks you can paste into your internal APM form.
- `pm_log_*.csv` — structured CSV logs for personal analysis.
- `pm_log_*.json` — JSON logs suitable for feeding to an LLM or integrating with future APIs.

## Suggested Workflow
1. During or after your shift, run the script and enter items as prompts.
2. Paste the generated APM block into the official form.
3. Keep the CSV/JSON for your own metrics and to populate memos or proposals.

## Policy & Security
- Confirm with your manager and security policies before introducing any automation or scripts on company hardware.
- Do **not** automate login/interaction with internal systems without written approval and an approved integration path.
- Keep logs free of sensitive data that shouldn't be stored locally.

## Next Steps (Optional)
- Use an LLM (e.g., Amazon Q in terminal) to transform your JSON log into bullet-proof summaries or to pre-fill text templates you paste into APM.
- If your org provides an official API, service, or bulk import, adapt the JSON to their schema.
