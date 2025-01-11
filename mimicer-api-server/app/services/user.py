from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import User
from app.util import password_hash as hasher
from app.util import jwt_token

def authenticate(db: Session,username:str, password: str):
    user = db.query(User).filter(
        or_(
            User.name == username,
            User.display_name == username
        )
    ).first()
    if user and hasher.verify_password(password,user.password):
            return user
    raise Exception("wrong username or password") 

def login(db:Session, username:str, password: str):
    result = authenticate(db,username,password)
    if result:
        return get_access_token(result)
    else:
        return result     

def get_access_token(user: User):
    if user:
        return jwt_token.create_access_token(user)
    else:
        raise Exception("No user found")