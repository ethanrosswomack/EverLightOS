#!/usr/bin/env python3
import boto3
import json

def test_basic_models():
    client = boto3.client('bedrock-runtime', region_name='us-east-1')

    basic_models = [
        'amazon.titan-text-express-v1',
        'anthropic.claude-3-haiku-20240307-v1:0',
        'anthropic.claude-3-5-sonnet-20240620-v1:0'
    ]

    for model_id in basic_models:
        try:
            if 'titan' in model_id:
                body = {"inputText": "Hello", "textGenerationConfig": {"maxTokenCount": 10}}
            elif 'claude' in model_id:
                body = {"messages": [{"role": "user", "content": "Hello"}], "max_tokens": 10, "anthropic_version": "bedrock-2023-05-31"}

            response = client.invoke_model(modelId=model_id, body=json.dumps(body))
            print(f"✅ {model_id} - WORKING!")

        except Exception as e:
            print(f"❌ {model_id} - {str(e)[:80]}")

if __name__ == "__main__":
    test_basic_models()
