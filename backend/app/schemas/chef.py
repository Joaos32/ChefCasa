from pydantic import BaseModel, EmailStr
from typing import Optional

class ChefBase(BaseModel):
    name: Optional[str] = None
    specialty: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    bio: Optional[str] = None
    available: Optional[bool] = None

class ChefCreate(ChefBase):
    name: str
    specialty: str
    email: EmailStr
    password: str  # Senha em texto puro (será hasheada)

class ChefResponse(ChefBase):
    id: int

    class Config:
        from_attributes = True

class ChefUpdate(ChefBase):  # Novo schema para atualização
    pass
