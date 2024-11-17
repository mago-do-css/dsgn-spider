# Usar uma imagem base com Python
FROM python:3.10-slim

# Configurar diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY . .

# Instalar as dependências do Python listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o driver MySQL (opcional, se não estiver no requirements.txt)
RUN pip install mysql-connector-python
# ou
RUN pip install pymysql

# Expor a porta da API
EXPOSE 5000  

# Comando para rodar a aplicação 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
