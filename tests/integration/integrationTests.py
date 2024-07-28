import requests

def test_get_status_code():
    response = requests.get('${aws_api_gateway_deployment.api_deployment.invoke_url}/statuscode', headers={'x-api-key': ''})
    assert response.status_code in [200, 300, 400, 500, 501, 503, 507]
    assert "Random status code" in response.json()['message']