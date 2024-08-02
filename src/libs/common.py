"""Module for a common function"""
import random


def get_random_status_code():
    """a common function to return a random code"""
    status_codes = [200, 300, 400, 500, 501, 503, 507]
    return random.choice(status_codes)
