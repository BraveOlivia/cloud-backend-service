from pydantic import BaseModel

class EventStats(BaseModel):
    total_events: int
    average_value: float | None
