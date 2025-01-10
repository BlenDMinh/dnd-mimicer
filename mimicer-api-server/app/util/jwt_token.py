from pydantic import BaseModel
from app.models import User
from datetime import datetime,timezone,timedelta
import env
import jwt
import json

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    display_name: str | None = None
    class Config:
        from_attributes = True

def create_access_token(user: User, expires_delta: timedelta | None = None):
    str_json = TokenData.model_validate(user).model_dump_json()
    print(str_json)
    data = json.loads(str_json)
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=3650)
    to_encode.update({"exp":expire})
    print(env.JWT_ALGO)
    encoded_jwt = jwt.encode(to_encode, env.JWT_KEY, algorithm=env.JWT_ALGO)
    return encoded_jwt