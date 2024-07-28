resource "aws_iam_role" "lambda_role" {
    name = "lambda-execution-role"
    assume_role_policy = jsonencode ({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

  managed_policy_arns = [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
  ]
}

resource "aws_lambda_function" "status_codes_function" {
  filename         = "lambdaFunction.zip"
  function_name    = "statusCodesFunction"
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_function.statusCodeHandler"
  source_code_hash = filebase64sha256("lambdaFunction.zip")
  runtime          = "python3.9"
}

resource "aws_api_gateway_rest_api" "status_codes_api" {
  name        = "statusCodesAPI"
  description = "API to return random HTTP status codes"
}

resource "aws_api_gateway_resource" "statuscode_resource" {
  rest_api_id = aws_api_gateway_rest_api.status_codes_api.id
  parent_id   = aws_api_gateway_rest_api.status_codes_api.root_resource_id
  path_part   = "statuscode"
}

resource "aws_api_gateway_method" "get_statuscode_method" {
  rest_api_id   = aws_api_gateway_rest_api.status_codes_api.id
  resource_id   = aws_api_gateway_resource.statuscode_resource.id
  http_method   = "GET"
  authorization = "NONE"
  api_key_required = true
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id = aws_api_gateway_rest_api.status_codes_api.id
  resource_id = aws_api_gateway_resource.statuscode_resource.id
  http_method = aws_api_gateway_method.get_statuscode_method.http_method
  type        = "AWS_PROXY"
  integration_http_method = "POST"
  uri         = aws_lambda_function.status_codes_function.invoke_arn
}

resource "aws_api_gateway_deployment" "status_codes_api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.status_codes_api.id
  stage_name  = "prod"
  depends_on = [
    aws_api_gateway_integration.lambda_integration
  ]
}

resource "aws_api_gateway_usage_plan" "usage_plan" {
  name = "usagePlan"
  api_stages {
    api_id = aws_api_gateway_rest_api.status_codes_api.id
    stage  = aws_api_gateway_deployment.status_codes_api_deployment.stage_name
  }
  throttle_settings {
    rate_limit = 3
    burst_limit = 5
  }
}

resource "aws_api_gateway_api_key" "api_key" {
  name = "APIKey"
  enabled = true
}

resource "aws_api_gateway_usage_plan_key" "usage_plan_key" {
  key_id = aws_api_gateway_api_key.id
  key_type = "API_KEY"
  usage_plan_id = aws_api_gateway_usage_plan.id
}

resource "aws_cloudwatch_metric_alarm" "5xx_alarm" {
  alarm_name          = "5xxErrorAlarm"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "1"
  metric_name         = "5xxError"
  namespace           = "AWS/ApiGateway"
  period              = "10"
  statistic           = "Sum"
  threshold           = "10"
  actions_enabled     = true
  alarm_actions       = []
  dimensions = {
    ApiName = aws_api_gateway_rest_api.status_codes_api.name
  }
}