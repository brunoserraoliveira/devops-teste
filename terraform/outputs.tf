output "api_url" {
  description = "URL da API"
  value       = aws_apigatewayv2_stage.api_stage.invoke_url
}

output "lambda_function_name" {
  description = "Nome da função Lambda"
  value       = aws_lambda_function.api_lambda.function_name
}

output "ecr_repository_url" {
  description = "URL do repositório ECR"
  value       = data.aws_ecr_repository.existing_repo.repository_url
}