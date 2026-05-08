from fastapi import FastAPI
from app.routers.auth import router

app = FastAPI()

app.include_router(router, prefix='/v1')
