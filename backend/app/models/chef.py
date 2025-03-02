from sqlalchemy import Column, Integer, String, Text, Boolean
from app.core.database import Base

class Chef(Base):
    __tablename__ = "chefs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)  # Especialidade culinária do chef
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)  # Telefone para contato
    password_hash = Column(String, nullable=False)
    bio = Column(Text, nullable=True)  # Biografia do chef
    available = Column(Boolean, default=True)  # Se está disponível para trabalho
