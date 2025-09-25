# Amazon RME BridgeOps - APM Assistant

Minimal APM workflow automation that integrates with existing Taskmonkey processes.

## Quick Start

```bash
make demo          # Full pipeline demo (rule-based)
make demo-q        # Demo with Amazon Q integration
make run-dry WO=X  # Test specific work order
make run-live WO=X # Execute live (manager approval required)
```

## Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ APM Export  │───▶│ Normalizer  │───▶│ Q Analyzer  │───▶│ Action Plan │
│ (CSV/API)   │    │ (canonical) │    │ (AI/Rules)  │    │ (JSON)      │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                   │
                                                                   ▼
┌─────────────┐    ┌─────────────┐                      ┌─────────────┐
│ Audit Log   │◀───│ Taskmonkey  │◀─────────────────────│ TM Adapter  │
│ (decisions) │    │ Runner      │                      │ (commands)  │
└─────────────┘    └─────────────┘                      └─────────────┘
```

## Components

- **Normalizer** (`src/normalize.py`) - Convert CSV to canonical schema
- **Q Client** (`src/q_client.py`) - Amazon Q integration with safe fallback
- **Planner** (`src/plan_stub.py`) - Generate action plans (rule-based + Q ready)
- **TM Adapter** (`src/tm_adapter.py`) - Convert plans to Taskmonkey commands
- **Synthetic Data** (`data/synthetic_apm.csv`) - Safe test data
- **Examples** (`examples/`) - Sample artifacts and outputs

## Data Policy

See [POLICY.md](POLICY.md) for security guidelines and off-site development rules.

## Development

This repo is containerized and ready for:
- GitHub Codespaces
- Fork to new repo
- USB/external testing
- Sandbox environments