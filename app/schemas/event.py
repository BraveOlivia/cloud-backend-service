from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    source_id: str
    category: str
    value: float

class EventResponse(EventCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

