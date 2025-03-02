from pydantic import BaseModel, EmailStr
from typing import Optional

class ChefBase(BaseModel):
    name: str
    specialty: str  # Tipo de culinária do chef
    email: EmailStr
    phone: Optional[str] = None  # Telefone de contato opcional
    bio: Optional[str] = None  # Biografia do chef

class ChefCreate(ChefBase):
    password: str  # Senha em texto puro (será hasheada)

class ChefResponse(ChefBase):
    id: int
    available: bool  # Indica se o chef está disponível para reservas

    class Config:
        from_attributes = True