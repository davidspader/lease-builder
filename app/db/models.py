from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)

class Template(Base):
    __tablename__ = 'templates'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    description = Column('description', String, nullable=False, unique=True)
    document_id =  Column('document_id', String, nullable=False, unique=True)
    user_id = Column('user_id', ForeignKey('users.id'), nullable=False)