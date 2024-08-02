import requests
import random
import os

API_URL = os.getenv('API_KEY')
API_KEY = os.getenv('API_KEY')


def test_api_endpoint():
    headers = {"x-api-key": API_KEY}
    response = requests.get(API_URL, headers=headers)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    status_code = response.json().get('statusCode')
    assert status_code in [200, 300, 400, 500, 501, 503, 507], f"Unexpected status code {status_code}"


def run_tests():
    test_api_endpoint()
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()