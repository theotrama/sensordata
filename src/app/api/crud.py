from sqlalchemy.orm import Session

from . import models, schemas


def get_sensor(db: Session, sensor_id: int):
    return db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()


def get_measurements(db: Session, start_id: int, end_id: int):
    """
    GET all measurements from start_id to end_id
    :param db:
    :param start_id:
    :param end_id:
    :return: QueryList
    """
    return db.query(models.Measurement).filter(models.Measurement.id == start_id).first()


def create_measurement(db: Session, measurement: schemas.MeasurementCreate):
    """
    POST a measurement to the database
    :param db: Database object
    :param measurement
    :return: db_measurement
    """
    db_measurement = models.Measurement(sensor_id=measurement.sensor_id, datapoint=measurement.datapoint)
    db.add(db_measurement)
    db.commit()
    db.refresh(db_measurement)
    return db_measurement
