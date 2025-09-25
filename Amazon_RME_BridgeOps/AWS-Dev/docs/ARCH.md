# Architecture

This document sketches the architecture for the local-first APM tooling that will be deployed to AWS serverless.

High-level:

- API Gateway receives HTTP requests from agents/clients.
- Lambda functions implement ingestion, processing, and API handlers.
- DynamoDB stores metrics, sessions, and metadata.
- Optional: S3 for artifacts, CloudWatch for logs and metrics, EventBridge for scheduling.

Components:

- api/
- lambdas/
- services/
- infra/ (CDK/CloudFormation/Terraform artifacts)

Security:

- No credentials in repo. Use IAM roles and environment variables injected at deploy time.

