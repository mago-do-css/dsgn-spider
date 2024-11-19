from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

# Carregar variáveis do .env
load_dotenv()

# Configuração da URL do banco de dados
DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

try:
    engine = create_engine(DATABASE_URL) 
 
except Exception as e:
    raise Exception(f"Erro ao conectar ao banco de dados: {e}")


# Configuração da fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definição dos modelos
Base = declarative_base()

# Dependência para gerenciamento de sessão no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()