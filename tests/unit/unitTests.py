from src.functions.getStatusCode.handler import statusCodeHandler

def testLambdaHandler():
    response = statusCodeHandler({}, {})
    assert response['statusCode'] in [200, 300, 400, 500, 501, 503, 507]
    assert "Random status code" in response['body']['message']