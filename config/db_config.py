from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from config.configs import settings

REDIS_URL = "localhost:6379"

pg_engine: AsyncEngine = create_async_engine(settings.DB_POSTGRES_URL)

PG_Session: AsyncSession = sessionmaker(
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
    bind=pg_engine
)