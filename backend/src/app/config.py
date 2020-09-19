import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    if os.getenv("FASTAPI_ENV") == "dev_docker":
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_DEV_DOCKER")
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_DEV_LOCAL")
