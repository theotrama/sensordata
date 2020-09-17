import datetime
from pydantic import BaseModel


class SensorBase(BaseModel):
    name: str
    type: str
    unit: str

    class Config:
        orm_mode = True


class Sensor(SensorBase):
    id: int
    date_added: datetime.datetime


class SensorCreate(SensorBase):
    pass


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
