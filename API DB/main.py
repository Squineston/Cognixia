from fastapi import FastAPI
from app.controllers import router as account_router
from app.database import Base, engine

# Automatically create tables in the database if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Bank API (With Database)")

app.include_router(account_router)

@app.get("/")
def health_check():
    return {"status": "API is up and running!"}