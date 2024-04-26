# app/models/profession.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Profession(Base):
    __tablename__ = 'professions'
    
    id = Column(Integer, primary_key=True)
    specialty_id = Column(Integer, ForeignKey('specialties.id'), nullable=False)
    name = Column(String, nullable=False)
    
    # Relationship to Specialty
    specialty = relationship('Specialty', back_populates='professions')