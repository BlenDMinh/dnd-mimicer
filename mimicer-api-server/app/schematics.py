from pydantic import BaseModel

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
    discriminator: str
    avatar: str
    bot: bool
    created_at: float
    display_name: str
    joined_at: float
    status: str

    class Config:
        from_attributes = True

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