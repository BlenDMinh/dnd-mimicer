import json
from fastapi import Depends
from fastapi.routing import APIRouter

from app.schemas.dndbeyond import DnDBeyondDiceLog
from app.redis import get_redis_client
from app.util.hash import crc32_hash
from app.services.discord import discord_service

router = APIRouter(prefix='/dndbeyond', tags=['dndbeyond'])

@router.get("/")
def get_dndbeyond():
    return {"message": "Hello from D&D Beyond!"}

@router.post("/dice-log")
async def post_dice_log(dice_log: DnDBeyondDiceLog, redis_client = Depends(get_redis_client)):
    hash_id = crc32_hash(dice_log.id)
    hash_session_id = crc32_hash(dice_log.session_id)

    if not redis_client.getbit('dndbeyond.session', hash_session_id):
        res = discord_service.create_session(dice_log.session_id)
        message_id = res['id']
        redis_client.setbit('dndbeyond.session', hash_session_id, 1)
        redis_client.set(f'dndbeyond.session.{hash_session_id}.message_id', message_id)

    if redis_client.getbit(hash_session_id, hash_id):
        return {"message": "Dice log already saved!"}

    message_id = int(redis_client.get(f'dndbeyond.session.{hash_session_id}.message_id'))
    initiative_json = redis_client.get(f'dndbeyond.session.{hash_session_id}.initiative')
    initiative = json.loads(initiative_json) if initiative_json else []

    log_json = redis_client.get(f'dndbeyond.session.{hash_session_id}.log')
    log = json.loads(log_json) if log_json else []

    log.append({
        "name": dice_log.name,
        "action": dice_log.action,
        "roll": dice_log.roll,
        "hidden": dice_log.hidden
    })
    # Get last 5
    log = log[-5:]

    if dice_log.action == "Initiative: roll":
        # Update initiative and sort
        for i in initiative:
            if i["name"] == dice_log.name:
                i["roll"] = dice_log.roll
                break
        else:
            initiative.append({
                "name": dice_log.name,
                "roll": dice_log.roll,
                "hidden": dice_log.hidden
            })

        initiative = sorted(initiative, key=lambda x: x["roll"], reverse=True)

    res = discord_service.update_session(message_id, dice_log.session_id, initiative, log)

    redis_client.set(f'dndbeyond.session.{hash_session_id}.initiative', json.dumps(initiative))
    redis_client.set(f'dndbeyond.session.{hash_session_id}.log', json.dumps(log))
    redis_client.setbit(hash_session_id, hash_id, 1)

    return {"message": "Dice log saved!"}


