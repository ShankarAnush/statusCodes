"""Module providing a function fetching random status codes."""
import json
import libs.common as lib


def status_code_handler():
    """Function returns a random status code."""
    random_status_code = lib.get_random_status_code()
    return {
        "statusCode": random_status_code,
        "body": json.dumps({
            "message": f"Random Status Code : {random_status_code}"
        })
    }
