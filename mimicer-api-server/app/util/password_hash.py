from passlib.context import CryptContext
from pydantic import BaseModel

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(pwd, hashed):
    return pwd_context.verify(pwd,hashed)

def get_pwd_hash(pwd):
    return pwd_context.hash(pwd)