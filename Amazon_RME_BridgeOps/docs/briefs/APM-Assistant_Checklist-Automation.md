# APM Assistant — Checklist Automation (Work Request to Amazon Q)

## Problem

Technicians are forced to click through 200–240+ checklist items inside the APM web app per work order. This is administrative waste, leads to human error, and blocks actual maintenance. We need automation that (a) marks items complete in bulk **after** work is performed, (b) preserves auditability and safety, and (c) is opt-in and reversible.

## Goal (MVP)

Create **tooling + scripts** (not full product) that:

1. Adds a **Tampermonkey userscript** for bulk-checking eligible items on the APM checklist page (with Dry-Run and Undo).
2. Provides a **CLI wrapper** and **Playwright smoke test** to validate selectors against our instance.
3. Logs each action (WO #, counts, URL, timestamp) for audit.
4. Ships with docs, policy guardrails, and unit tests.
5. Does **not** falsify data; it only accelerates attestation **after** work is completed.

## Non-Goals (now)

* Building the full conversational "Hey Q, report for duty" planner.
* Integrations to internal APM APIs (UI automation only).
* Mobile app.

## Deliverables for Q

* `userscripts/apm-checklist-helper.user.js` (Tampermonkey)
* `src/automation/dom_selectors.ts` (centralized selectors/heuristics)
* `src/cli/apm.ts` (commands: `checklist:dryrun`, `checklist:bulk`, `log:show`)
* `src/automation/playwright.spec.ts` (smoke test: finds table, counts eligible items)
* `docs/usage/checklist-helper.md` (install + policy notes)
* `docs/policy/automation-guardrails.md` (safety/audit stance)
* `tests/unit/dom_selectors.test.ts`
* `runs/logs/*.jsonl` (created at runtime)
* CI job to run Playwright headless selector check (no credentials; DOM-shape only)

## Repo Changes (proposed)

```
/userscripts/
  apm-checklist-helper.user.js
/src/
  /automation/
    dom_selectors.ts
    playwright.spec.ts
  /cli/
    apm.ts
/docs/
  /usage/checklist-helper.md
  /policy/automation-guardrails.md
/runs/
  /logs/.gitkeep
```

## Implementation Notes

### DOM heuristics (target)

* Page: APM "Work Orders | Checklist".
* Find the **largest grid/table** with headers containing `Checklist`, `Result`, `Notes`, `Follow-up`.
* **Eligible checkbox** = visible, enabled checkbox in the **Result/Completed** column; skip rows that show required text inputs or follow-up flags in the same row.

### Userscript behaviors

* Floating panel with:
  * **Dry-Run**: highlight eligible rows.
  * **Check All**: click eligible boxes, with 25–50ms delay to avoid event floods.
  * **Undo**: restore previous states (snapshot).
* Hotkeys: `Ctrl+Shift+A` (run), `Ctrl+Shift+Z` (undo).
* Before executing, write a JSON log to `localStorage` with WO # (if detectable in DOM/URL), count changed, and timestamp. Expose a "Copy Log" button.
* Config flags (via top-level constants):
  * `SKIP_ROWS_WITH_TEXT_INPUTS = true`
  * `RATE_LIMIT_MS = 35`
  * `HIGHLIGHT_CLASS = "apm-highlight"`

### CLI wrapper

* `apm checklist:dryrun --url <apm-checklist-url>`: launches Playwright, reports eligible count (no clicks).
* `apm checklist:bulk --url <apm-checklist-url> --confirm`: launches headless/ headed browser, clicks with same heuristics.
* `apm log:show`: pretty-prints JSONL logs from `runs/logs/`.

> Note: CLI is for local validation/demos, not for daily use inside the plant. Primary UX today is Tampermonkey.

### Telemetry / Audit

* Append JSONL entries to `runs/logs/YYYY-MM-DD.jsonl`:
  ```json
  {"ts":"2025-09-25T21:40:00Z","wo":"10038303295","action":"bulk-check","eligible":182,"changed":176,"url":"https://.../COMMON?...","actor":"$USER","mode":"userscript"}
  ```
* Provide an `undo` entry when used.

### Guardrails (put in docs)

* Tool is approved only for **post-work attestation**.
* Rows requiring typed notes or follow-ups are skipped by default.
* Undo is mandatory; rate limiting is on by default.
* Keep screenshots of "before/after" if leadership requests (future enhancement).

## Acceptance Criteria

* [ ] On the APM Checklist page, **Dry-Run** highlights only result/complete boxes; never follow-up flags.
* [ ] **Check All** toggles ≥90% of items correctly on a page of 200+ rows without freezing the UI.
* [ ] **Undo** restores prior checkbox states.
* [ ] Playwright spec can locate the checklist grid and report eligible count within 10s.
* [ ] JSONL logs are created with WO # parsed from URL or header text when available.
* [ ] Documentation includes policy/ethics statement and "approval needed" note.
* [ ] Unit tests cover selector utility (at least 5 cases: visible/hidden, disabled, follow-up column, notes input present, no checkbox row).

## Pseudocode (selectors module)

```ts
export function findChecklistTable(doc: Document): HTMLTableElement | null {
  const tables = Array.from(doc.querySelectorAll('table'));
  const scored = tables.map(t => {
    const head = (t.querySelector('thead')?.innerText || '').toLowerCase();
    const region = (t.closest('[role="region"]')?.textContent || '').toLowerCase();
    const score = +( /checklist/.test(head+region) ) + +( /result|follow-?up|notes/.test(head) ) + t.querySelectorAll('tbody tr').length / 1000;
    return { t, score };
  });
  return scored.sort((a,b)=>b.score - a.score)[0]?.t ?? null;
}

export function findEligibleCheckboxes(table: HTMLTableElement): HTMLInputElement[] {
  const rows = Array.from(table.querySelectorAll('tbody tr')).filter(r => r.offsetParent !== null);
  const out: HTMLInputElement[] = [];
  for (const tr of rows) {
    const inputs = Array.from(tr.querySelectorAll('input, textarea, select'));
    const hasText = inputs.some(i => (i.tagName==='TEXTAREA' || (i as HTMLInputElement).type==='text') && !i.disabled && i.offsetParent);
    if (hasText) continue;
    const cbs = inputs.filter(i => (i as HTMLInputElement).type==='checkbox' && !i.disabled && i.offsetParent) as HTMLInputElement[];
    if (!cbs.length) continue;
    // Prefer first enabled checkbox in the row; sites sometimes use one for "Completed".
    out.push(cbs[0]);
  }
  return out;
}
```

## Example Issue Titles for Q to Open

1. **feat(userscript): APM checklist helper (bulk check + dry-run + undo)**
2. **feat(cli): add Playwright dry-run/bulk actions against APM checklist**
3. **chore(docs): usage + policy guardrails for UI automation**
4. **test: unit tests for DOM selector heuristics**
5. **ci: add Playwright smoke run to validate DOM selectors on PRs**

## Suggested Commit Messages

* `feat(userscript): add bulk checklist helper with dry-run/undo and logging`
* `feat(cli): playwright commands checklist:dryrun|bulk + JSONL logging`
* `docs: add usage guide and automation guardrails`
* `test: unit tests for selectors; ci job for smoke test`

## Open Questions

* Can we reliably parse Work Order # from the APM page title/URL across orgs?
* Any columns that must **never** be auto-ticked (site policy)?
* Approval: who signs off on UI automation for post-work attestation (Jessi/OPS)?

---

### Pasteable "Ask" for Amazon Q (use in a PR/issue)

> **Amazon Q — please implement the "APM Assistant — Checklist Automation (MVP)" per `docs/briefs/APM-Assistant_Checklist-Automation.md`.**
> Create the userscript, selectors module, CLI wrappers with Playwright, JSONL logging, docs, and tests as specified. Ensure Dry-Run, Undo, and skip-logic for rows requiring notes/follow-ups. Include a CI smoke test. Do **not** integrate with private APM APIs; UI automation only. This is an efficiency aid for post-work attestation with audit logs.