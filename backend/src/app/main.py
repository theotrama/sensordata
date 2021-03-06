from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.api import sensor, measurement
from app.config import Config
from .database import SessionLocal

app = FastAPI()


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    sensor.router,
    prefix="/api/sensors",
    tags=["sensors"],
)

app.include_router(
    measurement.router,
    prefix="/api/measurements",
    tags=["measurements"],
)
