from sqlalchemy import Column, Integer, DateTime, ForeignKey
from database import Base

class DownloadHistory(Base):
    __tablename__ = "download_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Referência a uma tabela `users`
    total_limit = Column(Integer, index=True)
    date_time_today = Column(DateTime, index=True)
