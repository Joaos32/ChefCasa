from sqlalchemy import Column, Integer, String, Boolean
from app.models.base import Base  # Certifique-se de que está correto!

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)  # Padrão mais usado
    is_chef = Column(Boolean, default=False)  # Indica se é um chef ou cliente
