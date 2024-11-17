from fastapi import FastAPI   
from app.Controller.OrderController import order_router

# Carregar as variáveis de ambiente do .env

app = FastAPI()

# Incluindo as rotas do controller
app.include_router(order_router, tags=["orders"])

@app.get("/order-teste")
def home():
    return {"message": "Hello World"}
