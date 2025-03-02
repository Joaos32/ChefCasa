from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str  # Senha em texto puro (iremos hashear depois)

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True

# Novas classes para autenticação
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
