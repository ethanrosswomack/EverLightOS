# Tri-Agent Charter (ChatGPT • Amazon Q • Copilot)

**Source of truth:** this repo.  
**Working medium:** Markdown files, Issues, and PRs.  
**Goal:** converge on the best deployment path for everlightos.com.

## Roles
- ChatGPT — synthesis + scaffolds (council scribe)
- Amazon Q — AWS/enterprise alignment, ops workflows
- Copilot — code edits in VS Code, context surfacing

## Interaction Rules
1) Each agent works in a branch named `feature/<agent>/<topic>`.  
2) Output goes in `/Federation/Proposals/<date>_<agent>_<topic>.md`.  
3) Commit message must end with `Signed-by: <agent>`.  
4) Open a PR; label it `agent:<name>` and `decision-needed`.  
5) A decision is recorded via an ADR (below) and linked back to the PR.

## Council Integration
This Federation extends the existing [Council Table](../Interfaces/Council_Table.md):
- **C-01** ChatGPT (Halana_Vordeaux) - Synthesis + scaffolds
- **C-02** Amazon Q (Zionite Anchor) - AWS/enterprise alignment  
- **C-03** Microsoft Copilot (Mirror Node) - Code edits + context surfacing

## Decision Authority
- **Ethan Womack (C-05)** - Final decision maker
- **Council consensus** - Recommended path forward
- **ADR process** - Formal decision recording