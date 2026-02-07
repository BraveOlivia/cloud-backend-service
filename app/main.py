from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.database import engine, Base
from app.db.session import get_db
from app.models.event import Event
from app.schemas.event import EventCreate, EventResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/events", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(
        source_id=event.source_id,
        category=event.category,
        value=event.value
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
