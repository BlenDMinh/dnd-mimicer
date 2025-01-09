from pydantic import BaseModel

class DnDBeyondDiceLog(BaseModel):
    id: str
    session_id: str
    name: str
    action: str
    roll: int
    hidden: bool

