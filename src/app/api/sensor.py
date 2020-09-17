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
