#!/usr/bin/env python3
"""
APM Data Normalizer - Convert raw CSV to canonical schema
"""
import csv
import json
import os
from pathlib import Path

def normalize_csv(input_path, output_path):
    """Convert raw APM CSV to normalized JSONL format"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(input_path, 'r') as csvfile, open(output_path, 'w') as jsonfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            normalized = {
                "work_order_id": row["work_order_id"],
                "org": row["org"],
                "priority": int(row["priority"]),
                "type": row["type"],
                "status": row["status"],
                "equipment": row["equipment"],
                "shift": row["shift"],
                "dept": row["dept"],
                "description": row["description"]
            }
            jsonfile.write(json.dumps(normalized) + '\n')

if __name__ == "__main__":
    input_file = "data/synthetic_apm.csv"
    output_file = "out/normalized.jsonl"
    normalize_csv(input_file, output_file)
    print(f"Normalized {input_file} -> {output_file}")