from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.Service.OrderService import OrderService

order_router = APIRouter()

class OrderController:

    # def __init__(self, db: Session = Depends(get_db)):  # Injeção de dependência para o banco de dados
    #     self.order_service = OrderService(db)

    def get_order(self, order_id: int):
        return self.order_service.get_order(order_id)

# Instanciando a controller e definindo a rota
@order_router.get("/order-service/{order_id}")
def get_order(order_id: int, controller: OrderController = Depends(OrderController)):
    return controller.get_order(order_id)
