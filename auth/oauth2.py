from email import header
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
SECRET_KEY = '5778449264e8e880cb8a2a73e58af572b88dffb43c979732ce43da043eb973b5'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_curreent_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  credentials_exception = HTTPException(
    status_code= status.HTTP_401_UNAUTHORIZED,
    detail= 'Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'}
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get('sub')
    if username is None:
      raise credentials_exception
    
  except JWTError:
    raise credentials_exception
  
  user = db_user.get_user_by_username(db, username)
  if user is None:
    raise credentials_exception
  
  return user