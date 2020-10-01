import os
from pathlib import Path

from dotenv import load_dotenv


# Create dotenv path and load environment variables
path = Path(os.path.abspath(__file__))


class Config:
    if os.getenv("FASTAPI_ENV") == "docker_dev":
        dotenv_path = os.path.join(path.parent.parent.parent, '.env.dev.db')
    elif os.getenv("FASTAPI_ENV") == "docker_prod":
        dotenv_path = os.path.join(path.parent.parent.parent, '.env.prod.db')
    else:
        dotenv_path = os.path.join(path.parent.parent.parent, '.env.local.db')

    load_dotenv(dotenv_path)
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    DB_URL = os.environ.get("DB_URL")
    DB_PORT = os.environ.get("DB_PORT")
    SQLALCHEMY_DATABASE_URI = f"postgres+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_URL}/{POSTGRES_DB}"
