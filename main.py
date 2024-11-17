from fastapi import FastAPI   
from app.Controller.OrderController import order_router

# Carregar as variáveis de ambiente do .env

app = FastAPI()

# Incluindo as rotas do controller
app.include_router(order_router, tags=["orders"])

@app.get("/")
def home():
    return {"message": "conectado com sucesso!"}
