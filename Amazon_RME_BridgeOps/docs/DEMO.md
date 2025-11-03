# Demo Guide

## Screenshots Needed

1. **Container Demo** - Terminal showing `make demo` execution
2. **Synthetic APM Table** - CSV data in spreadsheet view
3. **Generated Plans** - JSON output examples
4. **Taskmonkey Commands** - Dry-run output

## Demo Script

```bash
# 1. Show synthetic data
cat data/synthetic_apm.csv

# 2. Run full pipeline
make demo

# 3. Show generated artifacts
ls out/plans/
cat out/plans/10038554138.json

# 4. Test specific work order
make run-dry WO=10038554139

# 5. Show audit trail
cat logs/decisions.jsonl
```

## Key Talking Points

- **Safe Development** - No real APM data, containerized environment
- **Modular Architecture** - Each component has single responsibility
- **Q Integration Ready** - Switch from rules to AI with `--use-q` flag
- **Audit Trail** - All decisions logged for compliance
- **Taskmonkey Compatible** - Generates commands for existing workflow