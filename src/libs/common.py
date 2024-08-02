import random


def getRandomStatusCode():
    statusCodes = [200, 300, 400, 500, 501, 503, 507]
    return random.choice(statusCodes)
