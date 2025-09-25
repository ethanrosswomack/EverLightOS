import argparse, json, sys
from .core import Session, Header
from .storage import new_run_dir, save_all
from .schema import SESSION_SCHEMA

def validate_session(sess: Session) -> None:
    import jsonschema
    jsonschema.validate(sess.to_dict(), SESSION_SCHEMA)

def cmd_save(args):
    sess = get_sess()
    if getattr(args, "validate", False):
        try:
            validate_session(sess)
        except Exception as e:
            print(f"Schema validation failed: {e}")
            sys.exit(1)
    run_dir = new_run_dir(args.out)
    paths = save_all(sess, run_dir)
    print("Saved:")
    for k, v in paths.items():
        print(f" - {k}: {v}")

def main():
    # ... unchanged ...
    s = sub.add_parser("save", help="Save paste.txt, csv, json into runs/")
    s.add_argument("--out", help="Custom output directory")
    s.add_argument("--validate", action="store_true", help="Validate schema before saving")
    s.set_defaults(func=cmd_save)
    # ... unchanged ...