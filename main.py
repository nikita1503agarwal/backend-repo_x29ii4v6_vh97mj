from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from database import db
import os

app = FastAPI(title="NUPal API", version="0.1.0")

# CORS
frontend_url = os.getenv("FRONTEND_URL", "*")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url, "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    email: str
    password: str

@app.get("/")
async def root():
    return {"message": "NUPal API running"}

@app.get("/test")
async def test_db():
    try:
        collections = db.list_collection_names() if db else []
        return {
            "backend": "FastAPI",
            "database": "MongoDB",
            "database_url": os.getenv("DATABASE_URL", "unset"),
            "database_name": os.getenv("DATABASE_NAME", "unset"),
            "connection_status": "connected" if db else "not_configured",
            "collections": collections,
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/auth/login")
async def login(payload: LoginRequest):
    # Placeholder auth flow
    return {"ok": True, "email": payload.email}
