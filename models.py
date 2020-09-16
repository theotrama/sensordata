import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Sensor(Base):
    __tablename__ = 'sensors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    unit = Column(String)
    date_added = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Book(name='{self.name}', type='{self.type}', date_added={self.date_added})>"
