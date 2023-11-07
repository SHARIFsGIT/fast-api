from typing import List
from pydantic import BaseModel

# Article insed UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config():
        orm_mode= True
# Data that comes from the user
class UserBase(BaseModel):
    username: str
    email: str
    password: str
    
# Data that sends back to the user
class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    # This class sends back data to the user
    class Config():
        orm_mode= True

# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_mode= True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config():
        orm_mode= True