from fastapi import FastAPI
from app.Controller.OrderController import order_router
from dotenv import load_dotenv 
import os

# Carregar as variáveis de ambiente do .env

app = FastAPI()

# Incluindo as rotas do controller
app.include_router(order_router, prefix="/orders", tags=["orders"])

@app.get("/order-teste")
def home():
    return {"message": "Hello World"}
