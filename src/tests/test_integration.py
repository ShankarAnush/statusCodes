"""Integration test module"""
import os
import json
import pytest
import boto3
from botocore.exceptions import ClientError


def test_integration():
    """integration test in an AWS SDK for Python - boto3"""
    client = boto3.client(
        'lambda',
        region_name=os.getenv('AWS_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    try:
        response = client.invoke(
            FunctionName='status_code_handler',
            InvocationType='RequestResponse',
        )
        payload = json.loads(response['Payload'].read())
        status_code = payload.get('statusCode')
        print(f"Payload returned: {status_code}")
        expected_status_codes = {200, 300, 400, 500, 501, 503, 507}
        assert status_code in expected_status_codes, f"Unexpected payload: {status_code}"
    except ClientError as e:
        pytest.fail(f"Lambda invocation failed: {e}")
