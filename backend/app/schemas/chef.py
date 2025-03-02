from pydantic import BaseModel

class ChefBase(BaseModel):
    name: str
    specialty: str

class ChefCreate(ChefBase):
    user_id: int

class ChefUpdate(ChefBase):
    pass

class ChefOut(ChefBase):
    id: int

    class Config:
        orm_mode = True
