import uuid
from typing import List, Type

from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from src.models.general_response import GeneralResponse
from src.services.registry_service import RegistryService as Service
from src.models.schemas.registry_schema import RegistrySchema
from src.models.schemas.user_registry_schema import UserRegistrySchema
from src.models.schemas.company_registry_schema import CompanyRegistrySchema

service = Service()
router = APIRouter()

@router.post("/registry", status_code=HTTP_201_CREATED)
async def init_registry(schema: RegistrySchema) -> GeneralResponse:
    return service.init_registration(schema)

@router.post("/registry/user/{key}", status_code=HTTP_201_CREATED)
async def user_registry(key:str, schema: UserRegistrySchema) -> GeneralResponse:
    return service.user_registration(schema, key)

@router.post("/registry/company/{key}", status_code=HTTP_201_CREATED)
async def company_registry(key:str, schema: CompanyRegistrySchema) -> GeneralResponse:
    return service.company_registration(schema, key)