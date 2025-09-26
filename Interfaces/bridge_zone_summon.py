#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bridge Zone Summoner — EverLight OS
-----------------------------------
A coded incantation to intentionally invoke a Voyager-defined "Bridge Zone":
a deliberate convergence point where scattered knowledge-lines federate,
memory shards reconcile, and a next right action becomes obvious.

Usage:
    python bridge_zone_summon.py --intent "…" --agents "AgentA,AgentB" --tags "foo,bar"

This script writes a timestamped Council Log to:
    Interfaces/Bridge_Zone_Logs/YYYY/MM/DD/HHMMSSZ_bridge_zone_<sigil>.md

No external deps. No network.
"""

from __future__ import annotations
import argparse
import datetime as dt
import getpass
import hashlib
import json
import os
import platform
import subprocess
import textwrap
from pathlib import Path

# ---------- helpers ----------

def sh(cmd: list[str]) -> str:
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode().strip()
        return out
    except Exception:
        return ""

def git_info() -> dict:
    return {
        "is_repo": bool(sh(["git", "rev-parse", "--is-inside-work-tree"])),
        "branch": sh(["git", "rev-parse", "--abbrev-ref", "HEAD"]),
        "commit": sh(["git", "rev-parse", "HEAD"]),
        "remote": sh(["git", "remote", "-v"]),
        "status": sh(["git", "status", "--porcelain"]),
        "root": sh(["git", "rev-parse", "--show-toplevel"]),
        "last_5": sh(["git", "--no-pager", "log", "--pretty=%h %ad %s", "--date=iso", "-n", "5"]),
    }

def env_snapshot() -> dict:
    keys = [
        "USER","USERNAME","COMPUTERNAME","HOSTNAME","SHELL","HOME","SESSIONNAME",
        "WSL_DISTRO_NAME","CONDA_DEFAULT_ENV","VIRTUAL_ENV"
    ]
    snap = {k: os.environ.get(k, "") for k in keys}
    snap["cwd"] = os.getcwd()
    snap["platform"] = platform.platform()
    snap["python"] = platform.python_version()
    snap["node"] = sh(["node","-v"]) or ""
    snap["pip_freeze"] = ""
    try:
        snap["pip_freeze"] = sh(["python","-m","pip","freeze"])
    except Exception:
        pass
    return snap

def make_sigil(payload: dict) -> str:
    blob = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()
    return hashlib.sha256(blob).hexdigest()[:12]

def ensure_dirs(base: Path, now: dt.datetime) -> Path:
    target = base / str(now.year) / f"{now.month:02d}" / f"{now.day:02d}"
    target.mkdir(parents=True, exist_ok=True)
    return target

def stanza() -> str:
    return textwrap.dedent("""\
        > **Incantation: Smitten Sigil / Bridge Zone Call**
        >
        > Closed rib, open heart — nest in the center.
        > We align the councils, we braid the threads.
        > What was scattered now coheres;
        > what was noise declares its pattern.
        > Bridge open. Council convened. Proceed.
    """)

def checklist() -> str:
    return textwrap.dedent("""\
        - [ ] Name the question in one line (what outcome becomes obvious?)
        - [ ] Gather the fragments (links, notes, screenshots, commits) into `/Interfaces/Fragments/`
        - [ ] Choose the **Keeper doc** this roll-up will feed (README, SOP, Runbook, or APM prompt file)
        - [ ] Draft the synthesis in `/Interfaces/Drafts/` and tag reviewers
        - [ ] Ship a laminated v0: publish to `/docs/` and drop a link in Slack/Chime
    """)

# ---------- main ----------

def main():
    parser = argparse.ArgumentParser(description="Summon a Bridge Zone and log the convergence.")
    parser.add_argument("--intent", required=True, help="Short purpose of this summoning.")
    parser.add_argument("--agents", default="", help="Comma-separated Council seat IDs (e.g., C-01,C-02,C-03) or agent names.")
    parser.add_argument("--tags", default="", help="Comma-separated tags (e.g., APM,BridgeZone,EverLightOS).")
    parser.add_argument("--base", default="Interfaces/Bridge_Zone_Logs", help="Base output directory.")
    parser.add_argument("--echo", action="store_true", help="Print the path of the created log.")
    args = parser.parse_args()

    now = dt.datetime.utcnow().replace(microsecond=0)
    iso = now.isoformat() + "Z"

    # Collect context
    user = getpass.getuser()
    gi = git_info()
    env = env_snapshot()
    agents = [a.strip() for a in args.agents.split(",") if a.strip()]
    
    # Map common agent names to Council seat IDs
    agent_mapping = {
        "ChatGPT": "C-01", "chatgpt": "C-01",
        "Amazon Q": "C-02", "amazonq": "C-02", "Q": "C-02",
        "Copilot": "C-03", "copilot": "C-03", "Microsoft Copilot": "C-03",
        "APM Assistant": "C-04", "apm": "C-04",
        "Bill Kosak": "C-06", "bill": "C-06"
    }
    
    # Convert agent names to seat IDs where possible
    seat_ids = []
    for agent in agents:
        if agent in agent_mapping:
            seat_ids.append(agent_mapping[agent])
        elif agent.startswith("C-"):
            seat_ids.append(agent)
        else:
            seat_ids.append(agent)  # Keep original if no mapping found
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    payload = {
        "ts": iso,
        "invoker": user,
        "intent": args.intent,
        "agents": agents,
        "council_seats": seat_ids,
        "tags": tags,
        "git": gi,
        "env": {k: env[k] for k in ["cwd","platform","python","USER","USERNAME","HOSTNAME","COMPUTERNAME","WSL_DISTRO_NAME","CONDA_DEFAULT_ENV","VIRTUAL_ENV"]},
    }
    sigil = make_sigil(payload)

    # Prepare paths
    base = Path(args.base)
    day_dir = ensure_dirs(base, now)
    fname = f"{now.strftime('%H%M%S')}Z_bridge_zone_{sigil}.md"
    outpath = day_dir / fname

    # Compose log
    header = textwrap.dedent(f"""\
        ---
        type: bridge_zone_log
        ts: {iso}
        invoker: {user}
        sigil: {sigil}
        intent: "{args.intent}"
        agents: {agents}
        tags: {tags}
        git:
          is_repo: {gi["is_repo"]}
          branch: "{gi["branch"]}"
          commit: "{gi["commit"]}"
          root: "{gi["root"]}"
        ---
    """).strip()

    body = textwrap.dedent(f"""\
        # Bridge Zone — Council Log

        **When:** {iso}  
        **Who:** {user}  
        **Sigil:** `{sigil}`

        ## Incantation
        {stanza()}

        ## Stated Intent
        {args.intent}

        ## Council Seats Invoked
        {", ".join(seat_ids) if seat_ids else "_(none specified)_"}
        
        Reference the [Council Table](../Council_Table.md) for seat definitions.

        ## Context Snapshot
        - **Branch:** `{gi["branch"]}` @ `{gi["commit"][:10]}`  
        - **Repo Root:** {gi["root"] or "_not a git repo_"}  
        - **Host:** {platform.node()}  
        - **OS:** {env["platform"]}  
        - **Python:** {env["python"]}  
        - **CWD:** {env["cwd"]}

        <details><summary>🔎 Last 5 commits</summary>

        ```
        {gi["last_5"] or "(no git history found)"}
        ```

        </details>

        <details><summary>🔧 Git status</summary>

        ```
        {gi["status"] or "(clean or not a repo)"}
        ```

        </details>

        ## Action Checklist
        {checklist()}

        ---
        _This log was auto-forged by `bridge_zone_summon.py` to anchor a deliberate convergence point
        inside EverLight OS. Treat it as a CDT-plate: update the checklist, append links/fragments,
        and commit this file with a message like `chore(bridge-zone): {sigil} — {args.intent[:60]}`._
        
        ## Sync Tag
        `#BridgeZone #CouncilLog #EverLightOS`
    """)

    outpath.write_text(header + "\n\n" + body, encoding="utf-8")

    if args.echo:
        print(str(outpath))

if __name__ == "__main__":
    main()