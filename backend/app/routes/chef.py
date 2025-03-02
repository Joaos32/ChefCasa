from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.chef import ChefCreate, ChefResponse, ChefUpdate
from app.models.chef import Chef
from app.core.database import get_db
from app.core.security import hash_password

router = APIRouter(prefix="/chefs", tags=["Chefs"])

@router.get("/{chef_id}", response_model=ChefResponse)
def get_chef(chef_id: int, db: Session = Depends(get_db)):
    """Busca um chef pelo ID."""
    chef = db.query(Chef).filter(Chef.id == chef_id).first()
    if not chef:
        raise HTTPException(status_code=404, detail="Chef não encontrado")
    return chef

@router.put("/{chef_id}", response_model=ChefResponse)
def update_chef(chef_id: int, chef_data: ChefUpdate, db: Session = Depends(get_db)):
    """Atualiza os dados de um chef."""
    chef = db.query(Chef).filter(Chef.id == chef_id).first()
    if not chef:
        raise HTTPException(status_code=404, detail="Chef não encontrado")

    for key, value in chef_data.dict(exclude_unset=True).items():
        setattr(chef, key, value)

    db.commit()
    db.refresh(chef)
    return chef

@router.delete("/{chef_id}")
def delete_chef(chef_id: int, db: Session = Depends(get_db)):
    """Deleta um chef pelo ID."""
    chef = db.query(Chef).filter(Chef.id == chef_id).first()
    if not chef:
        raise HTTPException(status_code=404, detail="Chef não encontrado")

    db.delete(chef)
    db.commit()
    return {"message": "Chef deletado com sucesso"}
