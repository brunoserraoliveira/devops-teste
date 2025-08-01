variable "project_name" {
  description = "Nome do projeto"
  type        = string
  default     = "devops-test-api"
}

variable "environment" {
  description = "Ambiente"
  type        = string
  default     = "dev"
}

variable "aws_region" {
  description = "Região AWS"
  type        = string
  default     = "us-east-1"
}

variable "ecr_repository_url" {
  description = "URL do repositório ECR existente"
  type        = string
  default     = "288761769929.dkr.ecr.us-east-1.amazonaws.com/devops-test-api"
}