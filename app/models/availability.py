from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Availability(Base):
    __tablename__ = 'availability'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    monday = Column(String)  # Exemplo: 'morning', 'afternoon', 'evening'
    tuesday = Column(String)
    wednesday = Column(String)
    thursday = Column(String)
    friday = Column(String)
    saturday = Column(String)
    sunday = Column(String)

    user = relationship("User", back_populates="availability")

    def __repr__(self):
        return f"<Availability(user_id='{self.user_id}', monday='{self.monday}', ...)>"
