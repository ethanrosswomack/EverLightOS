#!/usr/bin/env python3
"""
Taskmonkey Adapter - Convert action plans to Taskmonkey commands
"""
import json
import shlex
import subprocess
import sys
from pathlib import Path

def run_plan(plan_file, dry_run=True):
    """Execute action plan via Taskmonkey commands"""
    with open(plan_file, 'r') as f:
        plan = json.load(f)
    
    print(f"=== Executing plan for WO {plan['work_order_id']} ===")
    print(f"Classification: {plan['classification']}")
    
    if plan.get('risk_flags'):
        print(f"⚠️  Risk flags: {', '.join(plan['risk_flags'])}")
    
    for i, step in enumerate(plan["steps"], 1):
        cmd = ["taskmonkey", "run", step["action"]]
        
        # Add fields as command arguments
        for k, v in (step.get("fields") or {}).items():
            cmd += [f"--{k}", str(v)]
        
        print(f"\nStep {i}: {step['why']}")
        print(f"CMD: {shlex.join(cmd)}")
        
        if not dry_run:
            try:
                subprocess.run(cmd, check=True)
                print("✓ Success")
            except subprocess.CalledProcessError as e:
                print(f"✗ Failed: {e}")
                return False
        else:
            print("(dry-run)")
    
    # Show parts and attachments
    if plan.get("parts_needed"):
        print(f"\n📦 Parts needed: {len(plan['parts_needed'])} items")
        for part in plan["parts_needed"]:
            print(f"  - {part['desc']} (qty: {part['qty']})")
    
    if plan.get("attachments"):
        print(f"\n📎 Attachments: {len(plan['attachments'])} items")
        for att in plan["attachments"]:
            print(f"  - {att['type']}: {att['template']}")
    
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python tm_adapter.py <plan_file> [--live]")
        sys.exit(1)
    
    plan_file = sys.argv[1]
    dry_run = "--live" not in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN MODE - No commands will be executed")
    else:
        print("🚀 LIVE MODE - Commands will be executed")
    
    success = run_plan(plan_file, dry_run)
    
    if success:
        print("\n✅ Plan execution completed")
    else:
        print("\n❌ Plan execution failed")
        sys.exit(1)

if __name__ == "__main__":
    main()