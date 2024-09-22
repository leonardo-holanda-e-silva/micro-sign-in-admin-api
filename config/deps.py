from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from config.db_config import PG_Session


async def get_pg_session() -> Generator:
    pg_session: AsyncSession = PG_Session

    try:
        yield pg_session
    finally:
        await pg_session.close()