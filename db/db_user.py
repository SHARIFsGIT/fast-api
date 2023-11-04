from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash

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
    return db.query(DbUser).filter(DbUser.id == id).first()
# for more filter: return db.query(DbUser).filter(DbUser.id == id).filter(DbUser.email == email).first()