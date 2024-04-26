# app/models/specialty.py
from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship
from .profession import Profession



class Specialty(Base):
    __tablename__ = 'specialties'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    
    
Specialty.professions = relationship('Profession', order_by=Profession.id, back_populates='specialty')
