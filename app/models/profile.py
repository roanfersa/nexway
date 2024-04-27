# app/models/profile.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from database import Base
from sqlalchemy.orm import relationship

class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    complete_name = Column(String, index=True)
    company_level = Column(String)  # Exemplo para 'market leader', 'market researching', 'scaling sales'
    product_service_type = Column(String)
    specialty = Column(String)
    profession = Column(String)
    meeting_preference = Column(String)  # Exemplo para 'remote', 'in-person', 'both'
    professional_experience = Column(String)  # Exemplo para 'less than 2 years', etc.
    networking_objective = Column(String)  # Exemplo para 'Financing', 'Investment', etc.
    # Adicionar campos adicionais conforme necessário
    

    # Aqui você pode adicionar relacionamentos se necessário, por exemplo:
    availability = relationship("Availability", back_populates="profile")
    # location = relationship("Location", back_populates="profile")
    # user = relationship("User", back_populates="profile")
