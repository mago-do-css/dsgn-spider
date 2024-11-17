from sqlalchemy import Column, Integer, String
from database import Base

class Order(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)
