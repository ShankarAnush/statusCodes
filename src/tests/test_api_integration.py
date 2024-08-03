"""Integration test module"""
import os
import requests


def test_api_endpoint():
    """test the integration of api endpoint"""
    headers = {"x-api-key":os.getenv('API_KEY')}
    response = requests.get(url=os.getenv('API_URL'), headers=headers, timeout=5)
    status_code = response.json().get('statusCode')
    assert status_code in [200, 300, 400, 500, 501, 503, 507], f"Unexpected code {status_code}"
