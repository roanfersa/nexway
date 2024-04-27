from sqlalchemy import Column, Integer, String
from database import Base

class ProductService(Base):
    __tablename__ = 'product_services'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<ProductService(name='{self.name}')>"
