from sqlalchemy.orm import relationship
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey

# This fields goes to the database
class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index= True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbArticle', back_populates='user')

class DbArticle(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index= True)
    titles = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("DbUser", back_populates='items')