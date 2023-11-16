from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)

class Template(Base):
    __tablename__ = 'templates'
    id =  Column('id', String, primary_key=True)
    description = Column('description', String, nullable=False, unique=True)