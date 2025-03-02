from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Chef(Base):
    __tablename__ = "chefs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)  # Tipo de culinária do chef
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)  # Telefone para contato
    password_hash = Column(String, nullable=False)
    bio = Column(Text, nullable=True)  # Biografia ou descrição do chef
    available = Column(Boolean, default=True)  # Se o chef está disponível para trabalho
    
    # Relacionamento futuro com reservas de clientes
    # bookings = relationship("Booking", back_populates="chef")
