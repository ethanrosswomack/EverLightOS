# Design Notes

This repo keeps data entry **local-first** and human-in-the-loop, producing standardized outputs:
- `apm_paste.txt` (for manual paste into internal APM)
- `pm_log.csv` and `pm_log.json`

Core modules:
- `core.py` — in-memory session model
- `storage.py` — save/load runs to `./runs/<timestamp>/`
- `schema.py` — JSON schema for validation
- `cli.py` — argparse-based interface

## AWS Port (future)
Target minimal serverless design:
- API Gateway (ingress)
- Lambda (validation + storage)
- DynamoDB (sessions/items)
- S3 (exports)
- Cognito/SSO for auth

Infrastructure via AWS CDK (TypeScript or Python).