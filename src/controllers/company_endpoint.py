import uuid
from typing import List

from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from src.services.company_service import CompanyService as Service
from src.models.company import Company
from src.models.schemas.company_schema import CompanySchema as Schema

service = Service()
router = APIRouter()

@router.post("/company", status_code=HTTP_201_CREATED)
async def create_company(schema: Schema):
    company = Company()
    company.name = schema.name
    return service.create_company(company)

@router.get("/company/{company_id}", response_model=Company)
async def get_company(company_id: uuid) -> Company:
    company = service.get_company(company_id)
    if company:
        return company
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Company not found")

@router.get("/companies", response_model=List[Company])
async def list_companies() -> List[Company]:
    companies = service.get_all_companies()
    return companies

@router.put("/company/{company_id}", response_model=Company)
async def update_company(company_id: uuid, schema: Schema):
    company = service.get_company(company_id)
    if company:
        company.name = schema.name
        return service.update_company(company)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Company not found")

@router.delete("/company/{company_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_company(company_id: uuid):
    company = service.get_company(company_id)
    if company:
        service.delete_company(company_id)
        return None
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Company not found")