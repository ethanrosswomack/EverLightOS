#!/usr/bin/env python3
"""
APM Action Planner - Generate action plans for work orders
"""
import json
import os
from pathlib import Path

def classify_work_order(wo):
    """Classify work order type"""
    wo_type = wo["type"].lower()
    if "preventive" in wo_type or "pm" in wo_type:
        return "PM"
    elif "safety" in wo_type or "inspection" in wo_type:
        return "Safety"
    else:
        return "CM"

def generate_plan(wo):
    """Generate action plan based on work order classification"""
    classification = classify_work_order(wo)
    
    base_plan = {
        "work_order_id": wo["work_order_id"],
        "classification": classification,
        "steps": [],
        "parts_needed": [],
        "attachments": [],
        "risk_flags": []
    }
    
    # Rule-based planning
    if classification == "PM":
        base_plan["steps"] = [
            {"action": "open_apm_wo", "why": "Access work order details", "fields": {"id": wo["work_order_id"]}},
            {"action": "open_pm_procedure", "why": "Load maintenance procedure", "fields": {"template": "pm_standard", "equip": wo["equipment"]}},
            {"action": "fill_checklist", "why": "Complete maintenance checklist", "fields": {"checklist": "pm_standard"}}
        ]
        base_plan["attachments"] = [{"type": "job_aid", "template": "pm_standard", "notes": "Standard PM procedure"}]
    
    elif classification == "Safety":
        base_plan["steps"] = [
            {"action": "open_apm_wo", "why": "Access work order details", "fields": {"id": wo["work_order_id"]}},
            {"action": "open_pm_procedure", "why": "Load safety procedure", "fields": {"template": "safety_inspection", "equip": wo["equipment"]}},
            {"action": "fill_checklist", "why": "Complete safety checklist", "fields": {"checklist": "safety_inspection"}}
        ]
        base_plan["risk_flags"] = ["requires_manager_review"]
    
    else:  # CM
        base_plan["steps"] = [
            {"action": "open_apm_wo", "why": "Access work order details", "fields": {"id": wo["work_order_id"]}},
            {"action": "request_parts", "why": "Check parts availability", "fields": {"equipment": wo["equipment"]}},
            {"action": "escalate_training", "why": "Verify technician qualification", "fields": {"equipment_type": wo["equipment"].split()[0]}}
        ]
        base_plan["parts_needed"] = [{"sku": "", "desc": "TBD based on diagnosis", "qty": 1}]
    
    return base_plan

def process_work_orders(input_file, output_dir, use_q=False):
    """Process normalized work orders and generate plans"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Import Q client if available
    try:
        from q_client import call_amazon_q
        q_available = True
    except ImportError:
        q_available = False
        print("Q client not available, using rule-based planning")
    
    with open(input_file, 'r') as f:
        for line in f:
            wo = json.loads(line.strip())
            
            if use_q and q_available:
                plan = call_amazon_q(wo, use_q=True)
            else:
                plan = generate_plan(wo)
            
            output_file = f"{output_dir}/{wo['work_order_id']}.json"
            with open(output_file, 'w') as plan_file:
                json.dump(plan, plan_file, indent=2)
            
            method = "Q" if (use_q and q_available) else "rules"
            print(f"Generated plan for WO {wo['work_order_id']} ({method})")

if __name__ == "__main__":
    import sys
    input_file = "out/normalized.jsonl"
    output_dir = "out/plans"
    use_q = "--use-q" in sys.argv
    
    if use_q:
        print("🤖 Using Amazon Q for planning")
    else:
        print("📋 Using rule-based planning")
    
    process_work_orders(input_file, output_dir, use_q)
    print(f"Plans saved to {output_dir}/")