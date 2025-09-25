#!/usr/bin/env python3
"""
Amazon Q Client - Safe Q/Bedrock integration for APM planning
"""
import json
import os
from typing import Dict, Any

# Q prompt template for deterministic output
Q_SYSTEM_PROMPT = """You are an APM operations assistant. You must output ONLY JSON matching the schema. 
Never include secrets or internal links. If info is missing, suggest next step without guessing."""

Q_USER_TEMPLATE = """Context:
- Role: Assist an RME tech by planning the next actions for each work order.
- Allowed actions: ["open_apm_wo","open_pm_procedure","fill_checklist","request_parts","escalate_training","attach_job_aid","close_wo_pending_review"]
- Constraints: Do not submit anything to production systems; produce an action plan for Taskmonkey to execute later.

Work Order:
{normalized_wo_json}

Output JSON schema:
{{
  "work_order_id": "...",
  "classification": "PM|CM|Safety",
  "steps": [
     {{"action": "<allowed action>", "why": "...", "fields": {{"...": "..."}}}}
  ],
  "parts_needed": [{{"sku":"", "desc":"", "qty":1}}],
  "attachments": [{{"type":"job_aid", "template":"", "notes":""}}],
  "risk_flags": ["missing_procedure|ambiguous_equipment|requires_manager_review"]
}}"""

def call_amazon_q(work_order: Dict[str, Any], use_q: bool = False) -> Dict[str, Any]:
    """
    Call Amazon Q for work order planning
    
    Args:
        work_order: Normalized work order JSON
        use_q: If True, call actual Q API; if False, use fallback logic
    
    Returns:
        Action plan JSON
    """
    if use_q and os.getenv('AWS_PROFILE'):
        try:
            import boto3
            
            # Initialize Q client (placeholder - adjust for actual Q API)
            client = boto3.client('bedrock-runtime', region_name='us-east-1')
            
            prompt = Q_USER_TEMPLATE.format(
                normalized_wo_json=json.dumps(work_order, indent=2)
            )
            
            # Bedrock Claude call (adjust model ID as needed)
            response = client.invoke_model(
                modelId='anthropic.claude-3-sonnet-20240229-v1:0',
                body=json.dumps({
                    'anthropic_version': 'bedrock-2023-05-31',
                    'max_tokens': 1000,
                    'system': Q_SYSTEM_PROMPT,
                    'messages': [{'role': 'user', 'content': prompt}]
                })
            )
            
            result = json.loads(response['body'].read())
            plan_json = json.loads(result['content'][0]['text'])
            
            # Log Q usage
            log_decision(work_order['work_order_id'], 'amazon_q', plan_json)
            return plan_json
            
        except Exception as e:
            print(f"Q API failed: {e}, falling back to rules")
            return _fallback_planning(work_order)
    else:
        return _fallback_planning(work_order)

def _fallback_planning(work_order: Dict[str, Any]) -> Dict[str, Any]:
    """Fallback rule-based planning when Q is unavailable"""
    from plan_stub import generate_plan
    plan = generate_plan(work_order)
    log_decision(work_order['work_order_id'], 'rule_based', plan)
    return plan

def log_decision(wo_id: str, method: str, plan: Dict[str, Any]):
    """Log planning decisions for audit trail"""
    os.makedirs('logs', exist_ok=True)
    
    log_entry = {
        'timestamp': __import__('datetime').datetime.now().isoformat(),
        'work_order_id': wo_id,
        'planning_method': method,
        'classification': plan.get('classification'),
        'steps_count': len(plan.get('steps', [])),
        'risk_flags': plan.get('risk_flags', [])
    }
    
    with open('logs/decisions.jsonl', 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

if __name__ == "__main__":
    # Test with sample work order
    sample_wo = {
        "work_order_id": "10038554138",
        "type": "Preventive maintenance",
        "equipment": "TPA4-pa6vra03 ARSAW 318"
    }
    
    plan = call_amazon_q(sample_wo, use_q=False)
    print(json.dumps(plan, indent=2))