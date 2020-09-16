from fastapi import FastAPI, APIRouter

from app.api import sensor

app = FastAPI()

app.include_router(sensor.router)
