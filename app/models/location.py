from database import Base
from sqlalchemy import Column, Integer, String, Float

class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    # Aqui você pode adicionar métodos representativos, como __repr__ ou __str__
    def __repr__(self):
        return f"<Location(name='{self.name}', latitude={self.latitude}, longitude={self.longitude})>"
