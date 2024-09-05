import uuid
from typing import List, Type

from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from src.services.system_service import SystemService as Service
from src.models.system import System
from src.models.schemas.system_schema import SystemSchema as Schema

service = Service()
router = APIRouter()

@router.post("/system", status_code=HTTP_201_CREATED)
async def create_system(schema: Schema):
    system = System()
    system.name = schema.name
    return service.create_system(system)

@router.get("/system/{system_id}", response_model=System)
async def get_system(system_id: uuid) -> Type[System] | None:
    system = service.get_system(system_id)
    if System:
        return system
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="System not found")

@router.get("/systems", response_model=List[System])
async def list_systems() -> list[Type[System]]:
    systems = service.get_all_systems()
    return systems

@router.put("/system/{system_id}", response_model=System)
async def update_system(system_id: uuid, schema: Schema) -> Type[System]:
    system = service.get_system(system_id)
    if system:
        system.name = schema.name
        return service.update_system(system)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="System not found")

@router.delete("/system/{system_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_system(system_id: uuid):
    system = service.get_system(system_id)
    if system:
        service.delete_system(system_id)
        return None
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="System not found")