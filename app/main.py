import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
import app.api.v1.endpoints as v1
from app.db.base import Base
from app.db.session import engine
from app.db.seed import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)  # Create tables
    seed_database()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(v1.router, prefix="/v1")


@app.get("/")
def root():
    return {"message": "Hello World"}
