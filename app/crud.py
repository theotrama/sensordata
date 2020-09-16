from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from api.models import Base, Sensor

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def add_sensor():
    s = Session()
    sensor = Sensor(
        name="home_sensor",
        type="temperature",
        unit="degree_celsius",
    )
    s.add(sensor)
    s.commit()


if __name__ == "__main__":
    # recreate_database()
    add_sensor()
