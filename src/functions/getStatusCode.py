import json
import libs.common as lib


def statusCodeHandler(event, context):
    randomStatusCode = lib.getRandomStatusCode()
    return {
        "statusCode": randomStatusCode,
        "body": json.dumps({
            "message": f"Random Status Code : {randomStatusCode}"
        })
    }
