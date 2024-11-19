from sqlalchemy.orm import Session
from database import SessionLocal
from app.Models.DownloadHistory import DownloadHistory

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

def get_download_history():
    # Criar uma sessão do banco
    db: Session = SessionLocal()
    try: 
        records = db.query(DownloadHistory).all()
        return records
    finally:
        db.close()