from fastapi import Request
from fastapi.routing import APIRouter

router = APIRouter(prefix='/interactions', tags=['interactions'])

@router.post("/")
def post_interactions(request: Request):
    return {
        "type": 1
    }