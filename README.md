# statusCodes
An application to expose RESTful API on AWS using AWS lambda functions 

## Features

- Returns random HTTP status codes: 200, 300, 400, 500, 501, 503, 507
- Uses AWS API Gateway for endpoint management
- Authenticates using an API key
- Includes CloudWatch alarm to monitor 5xx responses

## Prerequisites

- Python 3.9
- Terraform
- AWS CLI
- GitHub Actions

## Installations

- boto3: AWS SDK for Python
- pytest: To execute unit and integration tests
- requests: Library in Python to send/receive HTTP requests/responses

