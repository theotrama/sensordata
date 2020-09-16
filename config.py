import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # ToDo: Load from .env file in the future
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
