import json
import boto3
import datetime

# Lambda handler to create a task in DynamoDB table 'Tasks_Pro'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks_Pro')


def lambda_handler(event, context):
    # Validation
    if not event.get('body'):
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing request body'})
        }

    body = json.loads(event['body'])
    task_id = body.get('taskId')
    description = body.get('description')

    if not task_id or not description:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing taskId or description'})
        }

    # Auto-inject metadata
    timestamp = datetime.datetime.utcnow().isoformat()

    table.put_item(Item={
        'taskId': task_id,
        'description': description,
        'createdAt': timestamp,
        'status': 'PENDING'
    })

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Task Created Successfully',
            'id': task_id,
            'createdAt': timestamp
        })
    }
