# Amazon RME BridgeOps - APM Assistant

Minimal APM workflow automation that integrates with existing Taskmonkey processes.

## Architecture

```
APM Export → Normalizer → Q Analyzer → Action Plan → Taskmonkey Runner
```

## Quick Start

```bash
# Run full demo
make demo

# Generate plans only
make plan

# Test specific work order (dry-run)
make run-dry WO=10038554138

# Execute live (use with caution)
make run-live WO=10038554138
```

## Components

- **Normalizer** (`src/normalize.py`) - Convert CSV to canonical schema
- **Planner** (`src/plan_stub.py`) - Generate action plans (rule-based + Q integration ready)
- **Adapter** (`src/tm_adapter.py`) - Convert plans to Taskmonkey commands
- **Synthetic Data** (`data/synthetic_apm.csv`) - Safe test data

## Data Policy

See [POLICY.md](POLICY.md) for security guidelines and off-site development rules.

## Development

This repo is containerized and ready for:
- GitHub Codespaces
- Fork to new repo
- USB/external testing
- Sandbox environments