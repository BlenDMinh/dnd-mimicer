from fastapi import HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.exc import IntegrityError

from app.models import Channel
from app.schematics import ChannelSchema, UpdateBatchChannelSchema
from app.database import SessionDep

router = APIRouter(prefix='/channels', tags=['channel'])

@router.post("")
async def create_channel(channel: ChannelSchema, db: SessionDep):
    db.add(channel)
    db.commit()
    db.refresh(channel)
    return channel

@router.get("")
async def get_channels(db: SessionDep):
    channels = db.query(Channel).all()
    return channels

@router.delete("/{channel_id}")
async def delete_channel(channel_id: int, db: SessionDep):
    channel = db.get(Channel, channel_id)
    if channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    db.delete(channel)
    db.commit()
    return channel

@router.put("/update_batch")
async def update_batch(data: UpdateBatchChannelSchema, db: SessionDep):
    channels = data.channels
    updated_channels = []
    for channel_data in channels:
        db_channel = db.get(Channel, channel_data.id)
        if db_channel:
            # Update existing channel
            for key, value in channel_data.dict().items():
                setattr(db_channel, key, value)
            db.commit()
            db.refresh(db_channel)
            updated_channels.append(ChannelSchema.model_validate(db_channel).model_dump())
        else:
            # Create new channel if not found
            new_channel = Channel(**channel_data.model_dump())
            db.add(new_channel)
            try:
                db.commit()
                db.refresh(new_channel)
                updated_channels.append(ChannelSchema.model_validate(new_channel).model_dump())
            except IntegrityError:
                db.rollback()
                raise HTTPException(status_code=400, detail="Error while saving channel data")
    return updated_channels

@router.put("/{channel_id}")
async def update_channel(channel_id: int, channel: ChannelSchema, db: SessionDep):
    db_channel = db.get(Channel, channel_id)
    if db_channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    for key, value in channel.model_dump().items():
        setattr(db_channel, key, value)
    db.commit()
    db.refresh(db_channel)
    return db_channel
