from .database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default="now()")
    __table_args__ = {'extend_existing': True}

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default="now()")
    __table_args__ = {'extend_existing': True}