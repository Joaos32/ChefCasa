from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.core.database import get_db  # Ajuste aqui para evitar redefinição
from app.core.security import hash_password
from app.core.dependencies import get_current_user  # Ajuste correto da autenticação

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Cria um novo usuário com senha criptografada."""
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email já registrado")

    hashed_password = hash_password(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password  # Ajuste no nome do campo
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get("/me", response_model=UserRead)
def read_users_me(current_user: User = Depends(get_current_user)):
    """Retorna os dados do usuário autenticado."""
    return current_user
