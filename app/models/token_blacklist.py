from sqlalchemy import Column, Integer, DateTime, String
from database import Base
from datetime import datetime

class TokenBlacklist(Base):
    __tablename__ = 'token_blacklist'

    id = Column(Integer, primary_key=True, index=True)
    jti = Column(String, unique=True, nullable=False)  # JTI é o ID do token JWT
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<TokenBlacklist(jti='{self.jti}', created_at={self.created_at})>"
