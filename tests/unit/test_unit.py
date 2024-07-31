import pytest
from src.functions.getStatusCode import statusCodeHandler

def testLambdaHandler():
    response = statusCodeHandler({}, {})
    assert response['statusCode'] in [200, 300, 400, 500, 501, 503, 507]