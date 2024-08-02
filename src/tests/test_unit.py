import pytest
import src.functions.getStatusCode as func


def testLambdaHandler():
    response = func.statusCodeHandler({}, {})
    assert response['statusCode'] in [200, 300, 400, 500, 501, 503, 507]
