# app/models/attribute_weights.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class AttributeWeights(Base):
    __tablename__ = 'attribute_weights'
    
    id = Column(Integer, primary_key=True, index=True)
    attribute_name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    
    def __repr__(self):
        return f"<AttributeWeights(attribute_name='{self.attribute_name}', weight={self.weight})>"

 
networking_goal_id = Column(Integer, ForeignKey('networking_goals.id'))
networking_goal = relationship("NetworkingGoal", back_populates="attribute_weights")