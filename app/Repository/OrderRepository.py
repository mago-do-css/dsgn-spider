from sqlalchemy.orm import Session
from app.Models import History

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_order(self, order_id: int):
        return self.db.query(History).filter("user_id" == order_id).first()
