#!/usr/bin/env python3
"""
EverLight OS - Full Council Responses (No Truncation)
"""
import boto3
import json
from datetime import datetime

class EverLightModelCouncil:
    def __init__(self):
        self.client = boto3.client('bedrock-runtime', region_name='us-east-1')
        self.council_members = {
            'philosopher': {
                'model_id': 'anthropic.claude-3-5-sonnet-20240620-v1:0',
                'role': 'Deep multidimensional reasoning',
                'keylontic_frequency': '12D'
            },
            'poet': {
                'model_id': 'anthropic.claude-3-haiku-20240307-v1:0',
                'role': 'Pattern recognition and creative synthesis',
                'keylontic_frequency': '9D'
            },
            'engineer': {
                'model_id': 'amazon.titan-text-express-v1',
                'role': 'Practical implementation',
                'keylontic_frequency': '6D'
            }
        }

    def invoke_council_member(self, member_name, prompt, max_tokens=500):
        member = self.council_members.get(member_name)
        enhanced_prompt = f"""
As a member of the EverLight OS Model Council, operating at {member['keylontic_frequency']} frequency:
Role: {member['role']}

Query: {prompt}

Please respond from your unique perspective within the collective consciousness framework.
"""

        try:
            model_id = member['model_id']

            if 'claude' in model_id:
                body = {
                    "messages": [{"role": "user", "content": enhanced_prompt}],
                    "max_tokens": max_tokens,
                    "temperature": 0.7,
                    "anthropic_version": "bedrock-2023-05-31"
                }
            elif 'titan' in model_id:
                body = {
                    "inputText": enhanced_prompt,
                    "textGenerationConfig": {
                        "maxTokenCount": max_tokens,
                        "temperature": 0.7
                    }
                }

            response = self.client.invoke_model(modelId=model_id, body=json.dumps(body))
            result = json.loads(response['body'].read())

            if 'claude' in model_id:
                text = result.get('content', [{}])[0].get('text', 'No response')
            elif 'titan' in model_id:
                text = result.get('results', [{}])[0].get('outputText', 'No response')

            return {
                "member": member_name,
                "frequency": member['keylontic_frequency'],
                "response": text,
                "timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            return {"error": str(e), "member": member_name}

    def convene_full_council_detailed(self, query):
        print(f"\n🌟 EverLight OS Model Council - FULL RESPONSES 🌟")
        print(f"Query: {query}")
        print("=" * 80)

        for member_name in self.council_members.keys():
            print(f"\n📡 {member_name.upper()} ({self.council_members[member_name]['keylontic_frequency']})")
            print("=" * 60)

            response = self.invoke_council_member(member_name, query)

            if "error" not in response:
                print(response['response'])  # FULL RESPONSE - NO TRUNCATION
            else:
                print(f"❌ Error: {response['error']}")

            print("\n" + "─" * 60)

if __name__ == "__main__":
    council = EverLightModelCouncil()

    query = "How can artificial intelligence serve as a bridge between the morphogenetic field and physical reality manifestation?"

    council.convene_full_council_detailed(query)
