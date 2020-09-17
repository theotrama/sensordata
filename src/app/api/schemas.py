import datetime
from pydantic import BaseModel


class Sensor(BaseModel):
    id: int
    name: str
    type: str
    unit: str
    date_added: datetime.datetime

    class Config:
        orm_mode = True


class MeasurementBase(BaseModel):
    sensor_id: int
    datapoint: float

    class Config:
        orm_mode = True


class Measurement(MeasurementBase):
    id: int
    timestamp: datetime.datetime


class MeasurementCreate(MeasurementBase):
    pass
