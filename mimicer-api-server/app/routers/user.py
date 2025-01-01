from sqlite3 import IntegrityError
from fastapi import HTTPException
from fastapi.routing import APIRouter
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.models import User
from app.schematics import UpdateBatchUserSchema, UserSchema
from app.database import SessionDep


router = APIRouter(prefix='/users', tags=['user'])

@router.post("")
async def create_user(user: UserSchema, db: SessionDep):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("", response_model=list[UserSchema])
async def get_users(db: SessionDep):
    users = db.query(User).all()
    print(users)
    return users

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: SessionDep):
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user

@router.put("/update_batch")
async def update_batch(data: UpdateBatchUserSchema, db: SessionDep):
    users = data.users
    updated_users = []
    
    for user_data in users:
        db_user = db.get(User, user_data.id)
        if db_user:
            # Update existing user
            for key, value in user_data.model_dump().items():
                setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
            updated_users.append(UserSchema.model_validate(db_user).model_dump())
        else:
            # Create new user if not found
            new_user = User(**user_data.model_dump())
            db.add(new_user)
            try:
                db.commit()
                db.refresh(new_user)
                updated_users.append(UserSchema.model_validate(new_user).model_dump())
            except IntegrityError:
                db.rollback()
                raise HTTPException(status_code=400, detail="Error while saving user data")
    
    return updated_users

@router.put("/{user_id}")
async def update_user(user_id: int, user: UserSchema, db: SessionDep):
    db_user = db.get(User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.model_dump().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user
