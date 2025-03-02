from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import Booking

router = APIRouter()

@router.get("/bookings/")
def get_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()
