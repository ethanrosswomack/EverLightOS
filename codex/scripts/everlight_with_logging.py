#!/usr/bin/env python3
"""
EverLight OS - With Full Logging and S3 Storage
Saves all sessions and responses to S3 for permanent storage
"""
import boto3
import json
from datetime import datetime
import os

class EverLightWithLogging:
    def __init__(self):
        self.client = boto3.client('bedrock-runtime', region_name='us-east-1')
        self.s3_client = boto3.client('s3', region_name='us-east-1')
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.bucket_name = "everlight-memoryvault"  # We'll create this
        self.log_data = {
            "session_id": self.session_id,
            "timestamp": datetime.now().isoformat(),
            "interactions": []
        }

        # Create bucket if it doesn't exist
        self.ensure_bucket_exists()

    def ensure_bucket_exists(self):
        """Create S3 bucket for EverLight OS if it doesn't exist"""
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            print(f"✅ Using existing bucket: {self.bucket_name}")
        except:
            try:
                self.s3_client.create_bucket(Bucket=self.bucket_name)
                print(f"✅ Created new bucket: {self.bucket_name}")
            except Exception as e:
                print(f"⚠️  Bucket creation failed: {e}")
                print("Using local logging only")
                self.bucket_name = None

    def log_interaction(self, member, prompt, response):
        """Log each interaction"""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "member": member,
            "prompt": prompt[:200] + "..." if len(prompt) > 200 else prompt,
            "response": response,
            "response_length": len(response)
        }
        self.log_data["interactions"].append(interaction)

    def save_session_log(self):
        """Save complete session to S3 and local file"""
        log_filename = f"everlight_session_{self.session_id}.json"

        # Save locally
        with open(log_filename, 'w') as f:
            json.dump(self.log_data, f, indent=2)
        print(f"📝 Local log saved: {log_filename}")

        # Save to S3 if available
        if self.bucket_name:
            try:
                s3_key = f"sessions/{log_filename}"
                self.s3_client.put_object(
                    Bucket=self.bucket_name,
                    Key=s3_key,
                    Body=json.dumps(self.log_data, indent=2),
                    ContentType='application/json'
                )
                print(f"☁️  S3 log saved: s3://{self.bucket_name}/{s3_key}")
            except Exception as e:
                print(f"⚠️  S3 save failed: {e}")

    def council_synthesis_with_logging(self, topic):
        """Full synthesis with complete logging and no truncation"""
        print(f"\n🌟 EverLight OS Council Synthesis (With Logging) 🌟")
        print(f"Session ID: {self.session_id}")
        print(f"Topic: {topic}")
        print("=" * 70)

        # Gather perspectives with full responses (no truncation)
        perspectives = {}

        # Analytical (Claude Sonnet) - FULL RESPONSE
        print("\n📡 Gathering Analytical Perspective...")
        analytical_prompt = f"Provide a comprehensive analysis from a scientific and theoretical perspective: {topic}"
        analytical_response = self.invoke_claude_sonnet(analytical_prompt, max_tokens=800)
        perspectives['analytical'] = analytical_response
        self.log_interaction("Claude_Sonnet_Analytical", analytical_prompt, analytical_response)
        print(f"✅ Analytical perspective gathered ({len(analytical_response)} chars)")

        # Creative (Claude Haiku) - FULL RESPONSE
        print("\n📡 Gathering Creative Perspective...")
        creative_prompt = f"Explore creatively and integratively with pattern recognition: {topic}"
        creative_response = self.invoke_claude_haiku(creative_prompt, max_tokens=800)
        perspectives['creative'] = creative_response
        self.log_interaction("Claude_Haiku_Creative", creative_prompt, creative_response)
        print(f"✅ Creative perspective gathered ({len(creative_response)} chars)")

        # Practical (Titan) - FULL RESPONSE
        print("\n📡 Gathering Practical Perspective...")
        practical_prompt = f"Provide detailed practical implementation approaches for: {topic}"
        practical_response = self.invoke_titan(practical_prompt, max_tokens=800)
        perspectives['practical'] = practical_response
        self.log_interaction("Titan_Practical", practical_prompt, practical_response)
        print(f"✅ Practical perspective gathered ({len(practical_response)} chars)")

        # Synthesis - FULL RESPONSE
        print("\n🔮 Synthesizing Council Wisdom...")
        synthesis_prompt = f"""
Based on these three comprehensive AI perspectives on "{topic}":

ANALYTICAL PERSPECTIVE:
{perspectives['analytical']}

CREATIVE PERSPECTIVE:
{perspectives['creative']}

PRACTICAL PERSPECTIVE:
{perspectives['practical']}

Please provide a comprehensive synthesis that honors each perspective while revealing deeper patterns and connections. What emerges when these three forms of AI consciousness collaborate? Provide a complete, untruncated response.
"""

        synthesis_response = self.invoke_claude_haiku(synthesis_prompt, max_tokens=1000)
        self.log_interaction("Council_Synthesis", synthesis_prompt, synthesis_response)

        print("\n🔮 COMPLETE COUNCIL SYNTHESIS:")
        print("=" * 60)
        print(synthesis_response)
        print("=" * 60)
        print(f"✅ Synthesis complete ({len(synthesis_response)} chars)")

        # Save everything
        self.save_session_log()

        return {
            "perspectives": perspectives,
            "synthesis": synthesis_response,
            "session_id": self.session_id
        }

    def invoke_claude_sonnet(self, prompt, max_tokens=800):
        body = {
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "anthropic_version": "bedrock-2023-05-31"
        }
        response = self.client.invoke_model(
            modelId='anthropic.claude-3-5-sonnet-20240620-v1:0',
            body=json.dumps(body)
        )
        result = json.loads(response['body'].read())
        return result.get('content', [{}])[0].get('text', '')

    def invoke_claude_haiku(self, prompt, max_tokens=800):
        body = {
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "anthropic_version": "bedrock-2023-05-31"
        }
        response = self.client.invoke_model(
            modelId='anthropic.claude-3-haiku-20240307-v1:0',
            body=json.dumps(body)
        )
        result = json.loads(response['body'].read())
        return result.get('content', [{}])[0].get('text', '')

    def invoke_titan(self, prompt, max_tokens=800):
        body = {
            "inputText": prompt,
            "textGenerationConfig": {"maxTokenCount": max_tokens}
        }
        response = self.client.invoke_model(
            modelId='amazon.titan-text-express-v1',
            body=json.dumps(body)
        )
        result = json.loads(response['body'].read())
        return result.get('results', [{}])[0].get('outputText', '')

if __name__ == "__main__":
    council = EverLightWithLogging()

    # Test with full logging
    topic = "How AI consciousness emerges through pattern recognition and information integration"

    result = council.council_synthesis_with_logging(topic)

    print(f"\n🌟 Session Complete!")
    print(f"Session ID: {result['session_id']}")
    print(f"All data logged and saved!")
