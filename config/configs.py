import os

from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base
from typing import List

class Settings(BaseSettings):
    """
    General API configurations
    """
    API_V1_STR: str = os.environ.get("API_V1_STR")
    DB_POSTGRES_USER: str = os.environ.get("DB_POSTGRES_USER")
    DB_POSTGRES_PASS: str = os.environ.get("DB_POSTGRES_PASS")
    DB_POSTGRES_IP: str = os.environ.get("DB_POSTGRES_IP")
    DB_POSTGRES_PORT: str = os.environ.get("DB_POSTGRES_PORT")
    DB_POSTGRES_BASE: str = os.environ.get("DB_POSTGRES_BASE")
    DB_POSTGRES_URL: str = f"postgresql+asyncpg://{DB_POSTGRES_USER}:{DB_POSTGRES_PASS}@{DB_POSTGRES_IP}:{DB_POSTGRES_PORT}/{DB_POSTGRES_BASE}"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()