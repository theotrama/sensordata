import os
from pathlib import Path

from dotenv import load_dotenv


# Create dotenv path and load environment variables
path = Path(os.path.abspath(__file__))
dotenv_path = os.path.join(path.parent.parent, '.env')
load_dotenv(dotenv_path)


class Config:
    if os.getenv("FASTAPI_ENV") == "dev_docker":
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_DEV_DOCKER")
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_DEV_LOCAL")
