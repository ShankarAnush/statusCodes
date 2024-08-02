"""Integration test module"""
import os
import requests

API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')


def test_api_endpoint():
    """test the integration of api endpoint"""
    headers = {"x-api-key": API_KEY}
    response = requests.get(url=API_URL, headers=headers, timeout=5)
    assert API_KEY is not None, "API_KEY environment variable not set"
    assert API_URL is not None, "API_URL environment variable not set"

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

    status_code = response.json().get('statusCode')
    assert status_code in [200, 300, 400, 500, 501, 503, 507], f"Unexpected code {status_code}"
