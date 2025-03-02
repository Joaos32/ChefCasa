from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.chef import ChefCreate, ChefResponse
from app.models.chef import Chef
from app.core.database import get_db
from app.core.security import hash_password

router = APIRouter(prefix="/chefs", tags=["Chefs"])

def get_db():
    db = get_db()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ChefResponse)
def create_chef(chef: ChefCreate, db: Session = Depends(get_db)):
    """Cria um novo chef com senha criptografada."""
    if db.query(Chef).filter(Chef.email == chef.email).first():
        raise HTTPException(status_code=400, detail="Email já registrado")

    hashed_password = hash_password(chef.password)
    new_chef = Chef(name=chef.name, email=chef.email, password_hash=hashed_password, bio=chef.bio)
    db.add(new_chef)
    db.commit()
    db.refresh(new_chef)

    return new_chef

@router.get("/", response_model=list[ChefResponse])
def list_chefs(db: Session = Depends(get_db)):
    """Lista todos os chefs disponíveis."""
    return db.query(Chef).filter(Chef.available == True).all()
