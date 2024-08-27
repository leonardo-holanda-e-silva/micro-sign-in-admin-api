from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.company import Company
from src.models.schemas.company_schema import CompanySchema
from config.deps import get_pg_session

router = APIRouter()

