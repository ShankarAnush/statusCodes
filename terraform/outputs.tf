output "api_url" {
  value = "${aws_api_gateway_deployment.status_codes_api_deployment.invoke_url}/statuscode"
}