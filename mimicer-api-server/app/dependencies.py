from email.header import Header
from typing import Annotated

from fastapi import HTTPException
import env

def api_key_validation(api_key: Annotated[str | None, Header()] = None):
    if api_key is None:
        raise HTTPException(status_code=400, detail="API Key missing")
    if api_key != env.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key
