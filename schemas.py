from pydantic import BaseModel

# Data that comes from the user
class UserBase(BaseModel):
    username: str
    email: str
    password: str
    
# Data that sends back to the user
class UserDisplay(BaseModel):
    username: str
    email: str
    # This class sends back data to the user
    class Config():
        orm_mode= True