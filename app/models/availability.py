from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Availability(Base):
    __tablename__ = 'availability'

    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    day_of_week = Column(String, nullable=False)  # 'Segunda', 'Terça', etc.
    start_time = Column(Time, nullable=False)     # Horário de início da disponibilidade
    end_time = Column(Time, nullable=False)       # Horário de término da disponibilidade

    profile = relationship("Profile", back_populates="availability")

    def __repr__(self):
        return f"<Availability(profile_id='{self.profile_id}', day_of_week='{self.day_of_week}', start_time='{self.start_time}', end_time='{self.end_time}')>"

