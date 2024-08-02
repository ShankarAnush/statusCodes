output "api_url" {
  value       = "https://${aws_api_gateway_rest_api.status_codes_api.id}.execute-api.${var.region}.amazonaws.com/prod/statuscode"
  description = "URL for accessing the Status Codes API"
}

output "api_key_value" {
  value       = aws_api_gateway_api_key.api_key.value
  description = "API key for accessing the Status Codes API"
  sensitive   = true
}