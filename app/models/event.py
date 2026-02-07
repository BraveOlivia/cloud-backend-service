from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String, index=True)
    category = Column(String, index=True)
    value = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
