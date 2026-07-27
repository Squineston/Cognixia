from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import router as account_router

app = FastAPI(title="Simple Bank Application")

# Allow React app (running on localhost:3000 or 5173) to send requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account_router)