from fastapi import FastAPI
from app.db.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}
