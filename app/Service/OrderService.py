from app.Repository.OrderRepository import OrderRepository
from sqlalchemy.orm import Session

class OrderService:

    def __init__(self, db: Session): 
        self.order_repository = OrderRepository(db)


    def get_download_history(self):
        return self.order_repository.get_download_history()
