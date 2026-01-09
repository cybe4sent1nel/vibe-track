import json
import boto3
from decimal import Decimal

# Helper class to convert DynamoDB Decimal to float/int
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # convert to int when possible
            if obj % 1 == 0:
                return int(obj)
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks_Pro')


def lambda_handler(event, context):
    response = table.scan()
    items = response.get('Items', [])

    return {
        'statusCode': 200,
        'body': json.dumps({
            'count': len(items),
            'tasks': items
        }, cls=DecimalEncoder)
    }
