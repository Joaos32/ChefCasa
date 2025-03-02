from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import Chef

router = APIRouter()

@router.get("/chefs/")
def get_chefs(db: Session = Depends(get_db)):
    return db.query(Chef).all()
