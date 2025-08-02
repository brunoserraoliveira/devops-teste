# DevOps Test API

# Versão 1.0.0

**Autor:** Bruno Oliveira  
API Python serverless deployada na AWS usando Docker, Lambda, API Gateway e Terraform.

## 🚀 Endpoints Disponíveis

- **GET /** - Hello World padrão
- **GET /hello** - Retorna mensagem de hello
- **GET /echo?msg=texto** - Faz echo da mensagem
- **GET /health** - Health check da API

## 🏗️ Arquitetura

```
GitHub → Docker → ECR → Lambda → API Gateway
   ↓
Terraform Cloud (IaC)
```

## 🔧 Tecnologias

- **Python 3.9** - Linguagem da API
- **Docker** - Containerização
- **AWS Lambda** - Compute serverless
- **AWS API Gateway** - Exposição da API
- **AWS ECR** - Registry de containers
- **Terraform** - Infrastructure as Code
- **GitHub Actions** - CI/CD Pipeline

## 🌐 URL de Produção

https://km7l52whxa.execute-api.us-east-1.amazonaws.com/dev

## 🧪 Testes Locais

```bash
# Instalar dependências
cd api
pip install -r requirements.txt

# Executar testes
python -m pytest test_app.py -v
```

## 🚀 Deploy

O deploy é automático via GitHub Actions quando há push na branch `main`.

### Deploy Manual

```bash
# 1. Build e push da imagem
cd api
docker build -t 288761769929.dkr.ecr.us-east-1.amazonaws.com/devops-test-api:latest .
docker push 288761769929.dkr.ecr.us-east-1.amazonaws.com/devops-test-api:latest

# 2. Update da Lambda
aws lambda update-function-code \
  --function-name devops-test-api-function \
  --image-uri 288761769929.dkr.ecr.us-east-1.amazonaws.com/devops-test-api:latest
```

## 📊 Monitoramento

- **Logs da Lambda:** CloudWatch `/aws/lambda/devops-test-api-function`
- **Logs do API Gateway:** CloudWatch API Gateway execution logs

## 👨‍💻 Desenvolvedor

**Bruno Oliveira**  
Projeto de teste técnico DevOps - Arquitetura serverless completa com CI/CD

---

### 📋 Checklist do Projeto

- ✅ **API Python** funcionando
- ✅ **Container Docker** otimizado
- ✅ **AWS Lambda + API Gateway** deployado
- ✅ **Terraform** gerenciando infraestrutura
- ✅ **GitHub Actions** CI/CD pipeline
- ✅ **Documentação** completa
- ✅ **URLs funcionais** em produção

**Status:** 🎉 **COMPLETO E FUNCIONANDO**