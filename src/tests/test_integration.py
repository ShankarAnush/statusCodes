import pytest
import boto3
from botocore.exceptions import ClientError


def test_integration():
    client = boto3.client('lambda', region_name='us-west-2')
    try:
        response = client.invoke(
            FunctionName='statusCodeHandler',
            InvocationType='RequestResponse',
        )
        payload = response['Payload'].read()
        print(payload)
    except ClientError as e:
        pytest.fail(f"Lambda invocation failed: {e}")