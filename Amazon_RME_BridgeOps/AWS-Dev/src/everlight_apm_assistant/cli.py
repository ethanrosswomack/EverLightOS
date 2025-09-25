import argparse
import json
import sys
from .core import Session, Header
from .storage import new_run_dir, save_all
from .schema import SESSION_SCHEMA

_current: Session | None = None


def get_sess() -> Session:
    global _current
    if _current is None:
        # fallback empty
        _current = Session(Header(date=""))
    return _current


def cmd_new(args):
    global _current
    hdr = Header(
        date=args.date,
        site=args.site or "",
        area=args.area or "",
        shift=args.shift or "",
        tech_name=args.tech or "",
        manager_on_duty=args.mod or "",
        notes=args.notes or "",
    )
    _current = Session(hdr)
    print("Session created.")


def cmd_add(args):
    sess = get_sess()
    sess.add_item(
        equipment_id=args.equip,
        component=args.comp,
        action=args.action,
        result=args.result,
        time_spent_min=int(args.mins),
        work_order=args.wo or "",
        notes=args.notes or "",
    )
    print("Item added.")


def cmd_render(args):
    sess = get_sess()
    out = sess.render_text()
    print(out)


def cmd_save(args):
    sess = get_sess()
    if getattr(args, "validate", False):
        import jsonschema
        try:
            jsonschema.validate(sess.to_dict(), SESSION_SCHEMA)
        except Exception as e:
            print(f"Schema validation failed: {e}")
            sys.exit(1)
    run_dir = new_run_dir(args.out)
    paths = save_all(sess, run_dir)
    print("Saved:")
    for k, v in paths.items():
        print(f" - {k}: {v}")


def cmd_load(args):
    with open(args.path, "r", encoding="utf-8") as f:
        data = json.load(f)
    hdr = Header(**data["header"])
    s = Session(hdr)
    for it in data["items"]:
        s.add_item(**it)
    global _current
    _current = s
    print("Session loaded.")


def main():
    p = argparse.ArgumentParser(prog="apm-assistant", description="Local-first APM assistant")
    sub = p.add_subparsers(dest="cmd", required=True)

    n = sub.add_parser("new", help="Start a new session")
    n.add_argument("--date", required=True)
    n.add_argument("--site")
    n.add_argument("--area")
    n.add_argument("--shift")
    n.add_argument("--tech")
    n.add_argument("--mod")
    n.add_argument("--notes")
    n.set_defaults(func=cmd_new)

    a = sub.add_parser("add", help="Add an item")
    a.add_argument("--equip", required=True)
    a.add_argument("--comp", required=True)
    a.add_argument("--action", required=True)
    a.add_argument("--result", required=True)
    a.add_argument("--mins", default="5")
    a.add_argument("--wo")
    a.add_argument("--notes")
    a.set_defaults(func=cmd_add)

    r = sub.add_parser("render", help="Render paste block")
    r.set_defaults(func=cmd_render)

    s = sub.add_parser("save", help="Save paste.txt, csv, json into runs/")
    s.add_argument("--out", help="Custom output directory")
    s.add_argument("--validate", action="store_true", help="Validate schema before saving")
    s.set_defaults(func=cmd_save)

    l = sub.add_parser("load", help="Load from JSON")
    l.add_argument("--path", required=True)
    l.set_defaults(func=cmd_load)

    args = p.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()