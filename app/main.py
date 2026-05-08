from fastapi import FastAPI
from app.routers import auth, users

app = FastAPI()

app.include_router(auth.router, prefix='/v1')
app.include_router(users.router, prefix='/v1')

@app.get("/health")
def health():
    return {"status": "ok"}