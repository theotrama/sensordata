from sqlalchemy.orm import Session

from . import models, schemas


def get_sensor(db: Session, sensor_id: int):
    return db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()


def create_sensor(db: Session, sensor: schemas.SensorCreate):
    """
    POST a sensor to the database
    :param db: Database object
    :param sensor
    :return: Sensor object
    """
    db_sensor = models.Sensor(name=sensor.name, type=sensor.type, unit=sensor.unit)
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor


def get_sensors_by_id(db: Session, start_id: int, end_id: int):
    """
    GET all sensors from start_id to end_id
    :param db:
    :param start_id:
    :param end_id:
    :return: QueryList
    """
    return db.query(models.Sensor).filter(models.Sensor.id.between(start_id, end_id)).all()


def get_measurements_by_id(db: Session, start_id: int, end_id: int):
    """
    GET all measurements from start_id to end_id
    :param db:
    :param start_id:
    :param end_id:
    :return: QueryList
    """
    return db.query(models.Measurement).filter(models.Measurement.id.between(start_id, end_id)).all()


def get_all_measurements_by_sensor(db: Session, sensor_id):
    """
    GET all measurements of a specific sensor
    :param db:
    :param sensor_id:
    :return:
    """
    return db.query(models.Measurement).filter(models.Measurement.sensor_id == sensor_id).all()


def create_measurement(db: Session, measurement: schemas.MeasurementCreate):
    """
    POST a measurement to the database
    :param db: Database object
    :param measurement
    :return: Measurement object
    """
    db_measurement = models.Measurement(sensor_id=measurement.sensor_id, datapoint=measurement.datapoint)
    db.add(db_measurement)
    db.commit()
    db.refresh(db_measurement)
    return db_measurement
