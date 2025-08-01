terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.7.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket = "desafio-devops-selecao"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}
