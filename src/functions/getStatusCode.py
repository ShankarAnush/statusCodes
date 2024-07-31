import json
from src.libs.common import getRandomStatusCode

def statusCodeHandler(event, context):
    randomStatusCode = getRandomStatusCode
    return {
        "statusCode" : randomStatusCode,
        "body" : json.dumps({
            "message" : f"Random Status Code : {randomStatusCode}"
        })
    }