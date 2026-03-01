from pydantic import BaseModel, Field
from datetime import datetime

class EventCreate(BaseModel):
    source_id: str
    category: str
    value: float = Field(ge=0)


class EventResponse(EventCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

