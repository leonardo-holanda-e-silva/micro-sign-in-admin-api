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
    RABBIT_MQ_URL: str = os.environ.get("RABBIT_MQ_URL")
    RABBIT_MQ_REGISTRY_QUEUE: str = os.environ.get("RABBIT_MQ_REGISTRY_QUEUE")
    RABBIT_MQ_REGISTRY_DLQ: str = os.environ.get("RABBIT_MQ_REGISTRY_DLQ")
    MONGO_DB_USER: str = os.environ.get("MONGO_DB_USER")
    MONGO_DB_PASS: str = os.environ.get("MONGO_DB_PASS")
    MONGO_DB_IP: str = os.environ.get("MONGO_DB_IP")
    MONGO_DB_PORT: str = os.environ.get("MONGO_DB_PORT")
    MONGO_DB_REGISTRY_COLLECTION: str = os.environ.get("MONGO_DB_REGISTRY_COLLECTION")
    MONGO_DB_URL: str = f"mongodb://{MONGO_DB_USER}:{MONGO_DB_PASS}@{MONGO_DB_IP}:{MONGO_DB_PORT}/{MONGO_DB_REGISTRY_COLLECTION}"

    class Config:
        case_sensitive = True

settings = Settings()