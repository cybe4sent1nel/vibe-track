import json
import boto3

# Lambda handler to delete a task from DynamoDB table 'Tasks_Pro'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks_Pro')


def lambda_handler(event, context):
    if not event.get('body'):
        return { 'statusCode': 400, 'body': json.dumps({'error':'Missing Body'}) }

    body = json.loads(event['body'])
    task_id = body.get('taskId')
    if not task_id:
        return { 'statusCode': 400, 'body': json.dumps({'error':'Missing taskId'}) }

    table.delete_item(Key={'taskId': task_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Task {task_id} deleted'})
    }
