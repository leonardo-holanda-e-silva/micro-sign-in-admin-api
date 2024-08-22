from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.company import Company
from models.schemas.company_schema import CompanySchema
from config.deps import get_pg_session

router = APIRouter()

@router.get('/', status_code=status.HTTP_201_CREATED, response_model=CompanySchema)
async def get_companies(db: AsyncSession = Depends(get_pg_session())):
    async with db as session:
        query = select(Company)
        result = await session.execute(query)
        companies: List[Company] = result.scalars().all()

        return companies
