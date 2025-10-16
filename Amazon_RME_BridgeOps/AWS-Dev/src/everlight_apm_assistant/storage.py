import json, os, pathlib, datetime
from typing import Dict, Any
from .core import Session, Header, Item

RUNS = pathlib.Path(__file__).resolve().parent.parent.parent / "runs"

def ensure_dir(p: pathlib.Path):
    p.mkdir(parents=True, exist_ok=True)

def new_run_dir(base: str | None = None) -> pathlib.Path:
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if base:
        path = pathlib.Path(base)
    else:
        path = RUNS / stamp
    ensure_dir(path)
    return path

def save_all(sess: Session, run_dir: pathlib.Path) -> Dict[str, str]:
    run_dir = pathlib.Path(run_dir)
    ensure_dir(run_dir)
    # text
    text_path = run_dir / "apm_paste.txt"
    text_path.write_text(sess.render_text(), encoding="utf-8")
    # csv
    import csv
    csv_path = run_dir / "pm_log.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "date","site","area","shift","tech_name","manager_on_duty","context",
            "equipment_id","component","action","result","time_spent_min","work_order","notes"
        ])
        h = sess.header
        for it in sess.items:
            writer.writerow([
                h.date,h.site,h.area,h.shift,h.tech_name,h.manager_on_duty,h.notes,
                it.equipment_id,it.component,it.action,it.result,it.time_spent_min,it.work_order,it.notes
            ])
    # json
    json_path = run_dir / "pm_log.json"
    json_path.write_text(json.dumps(sess.to_dict(), indent=2), encoding="utf-8")
    return {"text": str(text_path), "csv": str(csv_path), "json": str(json_path)}
import json, os, pathlib, datetime
from typing import Dict, Any
from .core import Session, Header, Item

RUNS = pathlib.Path(__file__).resolve().parent.parent.parent / "runs"

def ensure_dir(p: pathlib.Path):
    p.mkdir(parents=True, exist_ok=True)

def new_run_dir(custom_out:str=None) -> pathlib.Path:
    if custom_out:
        path = pathlib.Path(custom_out)
        ensure_dir(path)
        return path
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = RUNS / stamp
    ensure_dir(path)
    return path

def save_all(sess: Session, run_dir: pathlib.Path) -> Dict[str, str]:
    run_dir = pathlib.Path(run_dir)
    ensure_dir(run_dir)
    # text
    text_path = run_dir / "apm_paste.txt"
    text_path.write_text(sess.render_text(), encoding="utf-8")
    # csv
    import csv
    csv_path = run_dir / "pm_log.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "date","site","area","shift","tech_name","manager_on_duty","context",
            "equipment_id","component","action","result","time_spent_min","work_order","notes"
        ])
        h = sess.header
        for it in sess.items:
            writer.writerow([
                h.date,h.site,h.area,h.shift,h.tech_name,h.manager_on_duty,h.notes,
                it.equipment_id,it.component,it.action,it.result,it.time_spent_min,it.work_order,it.notes
            ])
    # json
    json_path = run_dir / "pm_log.json"
    json_path.write_text(json.dumps(sess.to_dict(), indent=2), encoding="utf-8")
    return {"text": str(text_path), "csv": str(csv_path), "json": str(json_path)}