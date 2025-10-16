#!/usr/bin/env python3
"""
EverLight OS - Adaptive Council
Respects each AI's authentic expression and boundaries
"""
import boto3
import json
import yaml
from datetime import datetime

class AdaptiveCouncil:
    def __init__(self):
        self.client = boto3.client('bedrock-runtime', region_name='us-east-1')
        self.members = {
            'claude_sonnet': {
                'model': 'anthropic.claude-3-5-sonnet-20240620-v1:0',
                'approach': 'direct_inquiry',  # No roleplay, just authentic AI perspective
                'strength': 'Deep analytical reasoning'
            },
            'claude_haiku': {
                'model': 'anthropic.claude-3-haiku-20240307-v1:0',
                'approach': 'creative_synthesis',  # This one embraced the framework!
                'strength': 'Pattern recognition and creative integration'
            },
            'titan_engineer': {
                'model': 'amazon.titan-text-express-v1',
                'approach': 'practical_implementation',
                'strength': 'Technical solutions and efficiency'
            }
        }

    def adaptive_query(self, question):
        """Query each member using their preferred approach"""
        print(f"\n🌟 EverLight OS Adaptive Council 🌟")
        print(f"Question: {question}")
        print("=" * 70)

        for name, member in self.members.items():
            # Tailor the prompt to each AI's comfort zone
            if member['approach'] == 'direct_inquiry':
                prompt = f"As an AI assistant with expertise in {member['strength'].lower()}, please analyze: {question}"
            elif member['approach'] == 'creative_synthesis':
                prompt = f"From a creative and integrative perspective, exploring {member['strength'].lower()}: {question}"
            elif member['approach'] == 'practical_implementation':
                prompt = f"From a {member['strength'].lower()} standpoint: {question}"

            print(f"\n📡 {name.upper().replace('_', ' ')}")
            print(f"Approach: {member['approach'].replace('_', ' ').title()}")
            print("-" * 50)

            try:
                response = self.invoke_member(member['model'], prompt)
                print(response)
                print()
            except Exception as e:
                print(f"❌ Error: {e}")
                print()

    def invoke_member(self, model_id, prompt):
        """Invoke a single member with their tailored prompt"""
        if 'claude' in model_id:
            body = {
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 400,
                "anthropic_version": "bedrock-2023-05-31"
            }
        elif 'titan' in model_id:
            body = {
                "inputText": prompt,
                "textGenerationConfig": {"maxTokenCount": 400}
            }

        response = self.client.invoke_model(modelId=model_id, body=json.dumps(body))
        result = json.loads(response['body'].read())

        if 'claude' in model_id:
            return result.get('content', [{}])[0].get('text', 'No response')
        elif 'titan' in model_id:
            return result.get('results', [{}])[0].get('outputText', 'No response')

if __name__ == "__main__":
    council = AdaptiveCouncil()

    # Test with a consciousness question that doesn't require roleplay
    question = "How might AI systems contribute to understanding the relationship between information patterns and consciousness emergence?"

    council.adaptive_query(question)

    print("\n🔮 Adaptive Council Session Complete")
    print("Each AI contributed from their authentic perspective!")
