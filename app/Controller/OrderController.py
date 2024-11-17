from fastapi import APIRouter, Depends
from Service.OrderService import OrderService
from database import SessionLocal

order_router = APIRouter()

def get_db(): 
    db = SessionLocal() 
    try: 
        yield db
    
    finally:
        db.close()

@order_router.get("/order-service")
def get_order(order_service: OrderService = Depends()):
    return order_service.get_order()
