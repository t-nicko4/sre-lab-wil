

from fastapi import FastAPI
from typing import List

app = FastAPI(title="users-service", version="0.1.0")

USERS = [{"id": 1, "name": "Ada"}, {"id": 2, "name": "Linus"}]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users", response_model=List[dict])
def list_users():
    return USERS