from fastapi import HTTPException
from fastapi.routing import APIRouter
from app.models import CronJob
from app.schematics import CronJobCreate, CronJobSchema
from app.database import SessionDep

router = APIRouter(prefix='/cronjobs', tags=['cronjob'])

@router.post("")
async def create_cronjob(cronjob: CronJobCreate, db: SessionDep):
    cronjob = CronJob(**cronjob.model_dump())
    db.add(cronjob)
    db.commit()
    db.refresh(cronjob)
    return cronjob

@router.get("")
async def get_cronjobs(db: SessionDep):
    cronjobs = db.query(CronJob).all()
    return cronjobs

@router.delete("/{cronjob_id}")
async def delete_cronjob(cronjob_id: int, db: SessionDep):
    cronjob = db.get(CronJob, cronjob_id)
    if cronjob is None:
        raise HTTPException(status_code=404, detail="CronJob not found")
    db.delete(cronjob)
    db.commit()
    return cronjob
