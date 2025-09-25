import os, json, boto3

dynamodb = boto3.resource('dynamodb')
session_table = dynamodb.Table(os.environ['SESSION_TABLE'])
items_table = dynamodb.Table(os.environ['ITEMS_TABLE'])

def lambda_handler(event, context):
    path = event.get('resource', '')
    method = event.get('httpMethod', '')

    if path.endswith('/item') and method == 'POST':
        body = json.loads(event['body'])
        session_id = event['pathParameters']['id']
        item_id = body.get('item_id', None)
        if not item_id:
            import uuid
            item_id = str(uuid.uuid4())
        items_table.put_item(
            Item={
                'session_id': session_id,
                'item_id': item_id,
                **body
            }
        )
        return {"statusCode": 200, "body": json.dumps({"item_id": item_id})}

    elif path.endswith('/render') and method == 'GET':
        session_id = event['pathParameters']['id']
        resp = items_table.query(KeyConditionExpression='session_id = :sid',
                                ExpressionAttributeValues={':sid': session_id})
        items = resp.get('Items', [])
        # Simple render example
        lines = [f"{i['equipment_id']} | {i['component']} | {i['action']} -> {i['result']}" for i in items]
        return {"statusCode": 200, "body": "\n".join(lines)}

    return {"statusCode": 404, "body": "Not Found"}