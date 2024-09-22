from typing import Generator
import aioredis

from config.db_config import REDIS_URL
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_config import PG_Session

async def get_pg_session() -> Generator:
    pg_session: AsyncSession = PG_Session

    try:
        yield pg_session
    finally:
        await pg_session.close()

async def get_redis_session() -> Generator:
    redis = await aioredis.from_url(REDIS_URL)

    try:
        yield redis
    finally:
        await redis.close()