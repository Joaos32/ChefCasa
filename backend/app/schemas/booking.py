from pydantic import BaseModel
from datetime import date

class BookingBase(BaseModel):
    date: date

class BookingCreate(BookingBase):
    client_id: int
    chef_id: int

class BookingUpdate(BookingBase):
    pass

class BookingOut(BookingBase):
    id: int
    client_id: int
    chef_id: int

    class Config:
        orm_mode = True
