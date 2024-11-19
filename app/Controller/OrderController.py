from fastapi import APIRouter, Depends
from app.Service.OrderService import OrderService
import logging

logging.basicConfig(level=logging.DEBUG)

order_router = APIRouter()

class OrderController:
    def __init__(self, order_service: OrderService):
        self.order_service = order_service

def get_download_history(self, order_id: int):
    # Chama o serviço para buscar o pedido (sem mexer no banco aqui)
    return self.order_service.get_download_history()

# Criar dependência para o serviço
def get_service() -> OrderService:
    # Retornar uma instância do serviço
    return OrderService()

@order_router.get("/order-service/{order_id}")
def get_download_history(order_id: int, service: OrderService = Depends(get_service)):
    controller = OrderController(order_service=service)
    return controller.get_download_history(order_id)

@order_router.get("/order-intro")
def get_download_history_intro(controller: OrderController = Depends(get_service)):
    
    # records = controller.get_download_history() 
     
    return 'bucetinha'
