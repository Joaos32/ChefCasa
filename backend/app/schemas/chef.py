from pydantic import BaseModel, EmailStr
from typing import Optional

class ChefBase(BaseModel):
    name: str
    email: EmailStr
    bio: Optional[str] = None

class ChefCreate(ChefBase):
    password: str  # Senha em texto puro (será hasheada)

class ChefResponse(ChefBase):
    id: int
    available: bool

    class Config:
        from_attributes = True
