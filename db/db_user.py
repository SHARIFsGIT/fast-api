from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException, status

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username= request.username,
        email= request.email,
        password= Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# to read from database all users
def get_all_users(db: Session):
    return db.query(DbUser).all()

# to read from database one user
def get_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    # Handle any exception
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'User with {id} not found')
    return 
# for more filter: return db.query(DbUser).filter(DbUser.id == id).filter(DbUser.email == email).first()

# to update user
def update_user(db: Session, id: int, request: UserBase):
    user= db.query(DbUser).filter(DbUser.id == id)
    # Handle any exception
    if not user.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'User with {id} not found')
    return 
    user.update(
        {
            DbUser.username: request.username,
            DbUser.email: request.email,
            DbUser.password: Hash.bcrypt(request.password)
        }
    )
    db.commit()
    return 'ok'

# to delete user
def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    # Handle any exception
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'User with {id} not found')
    return 
    db.delete(user)
    db.commit()
    return 'ok'