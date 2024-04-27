# app/models/networking_goals.py

from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class NetworkingGoal(Base):
    __tablename__ = 'networking_goals'
    
    id = Column(Integer, primary_key=True, index=True)
    goal_name = Column(String, nullable=False)
    attribute_weights = relationship("AttributeWeight", back_populates="networking_goal")

    def __repr__(self):
        return f"<NetworkingGoal(goal_name='{self.goal_name}')>"
