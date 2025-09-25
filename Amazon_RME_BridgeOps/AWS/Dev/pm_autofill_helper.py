#!/usr/bin/env python3
import json
import csv
from datetime import datetime
import os

def prompt(msg, default=None):
    if default:
        v = input(f"{msg} [{default}]: ").strip()
        return v if v else default
    return input(f"{msg}: ").strip()

def yesno(msg, default="y"):
    d = "Y/n" if default.lower()=="y" else "y/N"
    v = input(f"{msg} ({d}): ").strip().lower()
    if v == "":
        return default.lower()=="y"
    return v in ["y","yes","1","true","t"]

def main():
    print("=== PM Entry Assistant ===")
    today = datetime.now().strftime("%Y-%m-%d")
    header = {
        "date": prompt("Date", today),
        "site": prompt("Site/Building (e.g., TPA4)", ""),
        "area": prompt("Area/Floor (e.g., 3rd floor)", ""),
        "shift": prompt("Shift (e.g., N2 Fri-Sat)", ""),
        "tech_name": prompt("Your name (for your log)", ""),
        "manager_on_duty": prompt("Manager on duty", ""),
        "notes": prompt("Shift context (optional)", ""),
    }

    items = []
    print("\nEnter PM items. Leave 'Equipment ID' empty to finish.\n")
    while True:
        equip = prompt("Equipment ID (e.g., Charger-36 / Drive-#### / Destacker-###)", "")
        if not equip:
            break
        comp = prompt("Component / Subsystem (e.g., fiducial, fan, filter, sensor)", "")
        action = prompt("Action taken (e.g., inspected, cleaned, replaced, aligned)", "")
        result = prompt("Result / Status (e.g., pass, restored, monitor)", "")
        time_spent = prompt("Time spent (mins)", "5")
        wo = prompt("Work order / ticket # (optional)", "")
        addl = prompt("Notes (optional)", "")

        items.append({
            "equipment_id": equip,
            "component": comp,
            "action": action,
            "result": result,
            "time_spent_min": time_spent,
            "work_order": wo,
            "notes": addl,
        })
        print("Item added.\n")

    # Write outputs
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = os.getcwd()
    text_path = os.path.join(outdir, f"apm_paste_{stamp}.txt")
    csv_path = os.path.join(outdir, f"pm_log_{stamp}.csv")
    json_path = os.path.join(outdir, f"pm_log_{stamp}.json")

    # (1) Formatted text block for APM paste
    lines = []
    lines.append(f"Date: {header['date']}   Site: {header['site']}   Area: {header['area']}   Shift: {header['shift']}")
    lines.append(f"Tech: {header['tech_name']}   MOD: {header['manager_on_duty']}")
    if header['notes']:
        lines.append(f"Context: {header['notes']}")
    lines.append("-" * 72)
    for i, it in enumerate(items, 1):
        lines.append(f"{i:02d}. {it['equipment_id']} | {it['component']} | {it['action']} -> {it['result']} "
                     f"(~{it['time_spent_min']}m){'  WO# '+it['work_order'] if it['work_order'] else ''}")
        if it['notes']:
            lines.append(f"    Notes: {it['notes']}")
    if not items:
        lines.append("(No PM items recorded)")
    text_block = "\n".join(lines)
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text_block)

    # (2) CSV log
    fieldnames = ["date","site","area","shift","tech_name","manager_on_duty","context",
                  "equipment_id","component","action","result","time_spent_min","work_order","notes"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for it in items:
            row = {
                "date": header["date"],
                "site": header["site"],
                "area": header["area"],
                "shift": header["shift"],
                "tech_name": header["tech_name"],
                "manager_on_duty": header["manager_on_duty"],
                "context": header["notes"],
                **it
            }
            writer.writerow(row)

    # (3) JSON for future automation
    payload = {
        "header": header,
        "items": items,
        "generated_at": datetime.now().isoformat()
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print("\nSaved:")
    print(f" - APM paste block: {text_path}")
    print(f" - CSV log:         {csv_path}")
    print(f" - JSON log:        {json_path}")
    print("\nCopy the contents of the APM paste block into your internal system as needed.")
    print("You can also feed the JSON to an LLM or future API script for templating or summaries.")

if __name__ == "__main__":
    main()
