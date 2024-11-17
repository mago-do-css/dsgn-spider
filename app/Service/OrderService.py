from app.Repository.OrderRepository import OrderRepository
from sqlalchemy.orm import Session

class OrderService:

    def __init__(self, db: Session): 
        self.order_repository = OrderRepository(db)


    def get_order(self, order_id: int):
        return self.order_repository.get_order(order_id)
