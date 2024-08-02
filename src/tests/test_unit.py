"""Unit test module"""
import functions.get_status_code as func


def test_lambda_handler():
    """function to test logic of the lambda unit"""
    response = func.status_code_handler()
    assert response['statusCode'] in [200, 300, 400, 500, 501, 503, 507]
