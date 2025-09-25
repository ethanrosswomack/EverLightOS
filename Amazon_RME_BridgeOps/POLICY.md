# Data Policy & Security Guidelines

## Off-Site Development Rules

### ✅ ALLOWED
- Code development and testing
- Synthetic/mock data (see `data/synthetic_apm.csv`)
- Containerized environments
- Private repository development
- Sandbox AWS profiles for Q/Bedrock testing

### ❌ PROHIBITED
- Real APM exports or work order data
- Internal Amazon system names or URLs
- Employee names or personal information
- Production AWS credentials
- Live system connections from external environments

## Data Hygiene

1. **Synthetic Data Only**: All test data must use fictional work orders, equipment IDs, and employee names
2. **No Real Exports**: Never copy actual APM data outside Amazon facilities
3. **Credential Isolation**: Use separate AWS profiles for external development
4. **Private Repos**: Keep repository private until management approval

## Approval Process

- Code review required before production deployment
- Manager sign-off needed for any live system integration
- Security review for any AWS service integration

## Audit Trail

All decisions and actions are logged to `logs/decisions.jsonl` for transparency and compliance.