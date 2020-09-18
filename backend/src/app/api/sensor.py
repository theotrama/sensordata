from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .import crud, schemas
from app.database_connection import get_db

router = APIRouter()


@router.get("/{sensor_id}", response_model=schemas.Sensor)
def read_sensor(sensor_id: int, db: Session = Depends(get_db)):
    sensor = crud.get_sensor(db, sensor_id=sensor_id)
    if sensor is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sensor


@router.get("/", response_model=List[schemas.Sensor])
def read_sensors(start_id: int = 0, end_id: int = 10, db: Session = Depends(get_db)):
    """
    GET list of sensors
    """
    sensors = crud.get_sensors_by_id(db, start_id=start_id, end_id=end_id)
    if not sensors:
        raise HTTPException(status_code=404, detail="User not found")
    return sensors


@router.post("/", response_model=schemas.SensorCreate)
async def create_sensor(sensor: schemas.SensorCreate, db: Session = Depends(get_db)):
    return crud.create_sensor(db=db, sensor=sensor)
