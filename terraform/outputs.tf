output "api_url" {
  value       = "${aws_api_gateway_deployment.status_codes_api_deployment.invoke_url}/statuscode"
  description = "URL for accessing the Status Codes API"
}

output "api_key_value" {
  value       = aws_api_gateway_api_key.api_key.value
  description = "API key for accessing the Status Codes API"
  sensitive   = true
}