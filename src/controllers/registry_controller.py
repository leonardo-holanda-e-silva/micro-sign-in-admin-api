import uuid
from typing import List, Type

from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from src.models.general_response import GeneralResponse
from src.services.mongo.mongo_service import MongoService
from src.services.registry_service import RegistryService
from src.models.schemas.registry_schema import RegistrySchema
from src.models.schemas.user_registry_schema import UserRegistrySchema
from src.models.schemas.company_registry_schema import CompanyRegistrySchema


class RegistryController:
    def __init__(self, mongo_service: MongoService, registry_service: RegistryService):
        self.router = APIRouter()
        self.mongo_service = mongo_service
        self.registry_service = registry_service

        # Definindo as rotas com URLs diferentes para evitar conflitos
        self.router.post("/registry", status_code=HTTP_201_CREATED)(self.init_registry)
        self.router.post("/registry/user/{key}", status_code=HTTP_201_CREATED)(self.user_registry)
        self.router.post("/registry/company/{key}", status_code=HTTP_201_CREATED)(self.company_registry)

    async def init_registry(self, schema: RegistrySchema) -> GeneralResponse:
        return self.registry_service.init_registration(schema)

    async def user_registry(self, key: str, schema: UserRegistrySchema) -> GeneralResponse:
        return self.registry_service.user_registration(schema, key)

    async def company_registry(self, key: str, schema: CompanyRegistrySchema) -> GeneralResponse:
        return self.registry_service.company_registration(schema, key)
