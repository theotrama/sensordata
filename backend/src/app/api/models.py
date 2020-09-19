import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey

Base = declarative_base()


class Sensor(Base):

    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    unit = Column(String)
    date_added = Column(DateTime, default=datetime.datetime.utcnow)
    date_add2ed = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Sensor(name='{self.name}', type='{self.type}', date_added={self.date_added})>"


class Measurement(Base):

    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer, ForeignKey('sensors.id', ondelete='CASCADE'))
    datapoint = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Measurement(data='{self.datapoint}', timestamp='{self.timestamp}', sensor_id={self.sensor_id})>"
