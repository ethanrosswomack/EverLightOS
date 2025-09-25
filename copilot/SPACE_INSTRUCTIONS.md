Goal: Design local-first APM tooling → AWS serverless (API Gateway + Lambda + DynamoDB).

Entry files:
- README.md
- docs/ARCH.md
- src/**
- examples/sample_session.json
- aws/blueprints/**

Rules:
- No internal credentials, keys, or system automation in this repo.
- Anonymize all example data and scrub PII before committing.

Tasks Copilot may do:
- Generate unit / integration tests and test harnesses.
- Create stricter JSON/YAML schema and validation code.
- Produce CDK skeletons for API Gateway + Lambda + DynamoDB.
- Draft docs and architecture diagrams from code and comments.

Pinned files for this Space (ensure these exist and are authoritative):
- `Amazon_RME_BridgeOps/AWS-Dev/README.md`
- `Amazon_RME_BridgeOps/AWS-Dev/docs/ARCH.md`
- `Amazon_RME_BridgeOps/AWS-Dev/src/everlight_apm_assistant/cli.py`
- `Amazon_RME_BridgeOps/AWS-Dev/src/everlight_apm_assistant/core.py`
- `Amazon_RME_BridgeOps/AWS-Dev/src/everlight_apm_assistant/schema.py`
- `Amazon_RME_BridgeOps/AWS-Dev/aws/blueprints/README.md`
- `Amazon_RME_BridgeOps/AWS-Dev/examples/sample_session.json`

How to start (first hour):
1. Open `Amazon_RME_BridgeOps/AWS-Dev` in the Copilot Space.
2. Run the devcontainer to get AWS CLI, CDK, Terraform, and `amazonq` available.
3. Ask Copilot to scaffold a CDK stack: "Create CDK skeleton for APIGW -> Lambda -> DDB".
4. Add tests and a simple example invocation in `examples/sample_session.json`.

Safety: If you find secrets in git history, rotate them immediately and follow the repo security checklist.
