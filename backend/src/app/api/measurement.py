from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .import crud, schemas
from app.database_connection import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Measurement])
async def read_measurements(start_id: int = 0, end_id: int = 10, db: Session = Depends(get_db)):
    measurements = crud.get_measurements_by_id(db, start_id=start_id, end_id=end_id)
    if not measurements:
        raise HTTPException(status_code=404, detail="Measurements not found")
    return measurements


@router.post("/", response_model=schemas.MeasurementCreate)
async def create_measurement(measurement: schemas.MeasurementCreate, db: Session = Depends(get_db)):
    db_sensor = crud.get_sensor(db, sensor_id=measurement.sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Related sensor not found")
    return crud.create_measurement(db=db, measurement=measurement)
