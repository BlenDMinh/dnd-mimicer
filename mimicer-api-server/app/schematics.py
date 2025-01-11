from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import time as Time, datetime
from app.util import password_hash as hasher
from app.models import UserRole, UserStatus

class CronJobBase(BaseModel):
    cron_expression: str
    function: str

class CronJobCreate(CronJobBase):
    pass

class CronJobSchema(CronJobBase):
    id: int

    class Config:
        from_attributes = True

class UserSchema(BaseModel):
    id: str
    name: str
    discriminator: UserRole
    avatar: str
    bot: bool
    display_name: str
    joined_at: datetime
    status: UserStatus
    password: str
    class Config:
        from_attributes = True

class UserInputSchema(BaseModel):
    name: str
    discriminator: UserRole
    display_name: str
    status: str
    password: str
    status: UserStatus
    bot: bool
    class Config:
        from_attributes = True
    
    @model_validator(mode='before')
    def hash_password(cls, values):
        if isinstance(values, dict) and values.get('password'):
            values['password'] = hasher.get_pwd_hash(values.get('password'))
        return values

class UserLogInSchema(BaseModel):
    username: str
    password: str

class UserOutputSchema(UserSchema):
    id: str

class UpdateBatchUserSchema(BaseModel):
    users: list[UserSchema]

class ChannelSchema(BaseModel):
    id: str
    name: str
    created_at: float
    type: int

    class Config:
        from_attributes = True

class UpdateBatchChannelSchema(BaseModel):
    channels: list[ChannelSchema]

# Storing free schedule

class ScheduleSchema(BaseModel):
    id: str
    user: UserSchema
    isPreset: bool
    year: Optional[int]
    weekOfYear: Optional[int]
    dayOfWeek: Optional[int]
    startTime: Time
    endTime: Time
    class Config:
        from_attributes = True

class DnDSessionSchema(BaseModel):
    id: str
    year: int
    weekOfYear: int
    dayOfWeek: int
    startTime: Time
    endTime: Time
    duration: int
    attendants: list[UserSchema]
    unattendants: list[UserSchema]
    detail: str
