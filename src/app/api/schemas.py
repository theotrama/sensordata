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


class Measurement(BaseModel):
    id: int
    sensor_id: int
    datapoint: float
    timestamp: datetime.datetime

    class Config:
        orm_mode = True
