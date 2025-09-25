# AWS Blueprints (Future)

This folder contains notes and skeletons to port the local tool to a serverless API.

## Minimal Architecture
- Amazon API Gateway
- AWS Lambda (Python)
- Amazon DynamoDB (session + items tables)
- Amazon S3 (artifacts)
- AWS IAM + SSO

Use CDK to define infra. Start with a single `POST /session/{id}/item` and `GET /session/{id}/render`.