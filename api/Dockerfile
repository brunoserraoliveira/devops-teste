FROM public.ecr.aws/lambda/python:3.9

# Copiar requirements e instalar dependências
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt --no-cache-dir

# Copiar código da aplicação
COPY app.py ${LAMBDA_TASK_ROOT}

# Definir o handler
CMD ["app.handler"]