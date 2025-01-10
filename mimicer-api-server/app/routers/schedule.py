from fastapi import HTTPException
from fastapi.routing import APIRouter
from app.schematics import ScheduleSchema
from typing import List
from app.database import SessionDep


router = APIRouter(prefix="/schedule",tags=['schedule'])

@router.post("")
async def create_schedule(schedules: List[ScheduleSchema], db: SessionDep):
    db.add(schedules)
    db.commit()
    db.refresh()
    return db