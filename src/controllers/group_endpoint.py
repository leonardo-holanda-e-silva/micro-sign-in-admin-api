import uuid
from typing import List, Type

from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from src.services.group_service import GroupService as Service
from src.models.group import Group
from src.models.schemas.group_schema import GroupSchema as Schema

service = Service()
router = APIRouter()

@router.post("/group", status_code=HTTP_201_CREATED)
async def create_group(schema: Schema):
    group = Group()
    group.name = schema.name
    return service.create_group(group)

@router.get("/group/{group_id}", response_model=Group)
async def get_group(group_id: uuid) -> Type[Group] | None:
    group = service.get_group(group_id)
    if Group:
        return group
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Group not found")

@router.get("/groups", response_model=List[Group])
async def list_groups() -> list[Type[Group]]:
    groups = service.get_all_groups()
    return groups

@router.put("/group/{group_id}", response_model=Group)
async def update_group(group_id: uuid, schema: Schema) -> Type[Group]:
    group = service.get_group(group_id)
    if group:
        group.name = schema.name
        return service.update_group(group)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Group not found")

@router.delete("/group/{group_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_group(group_id: uuid):
    group = service.get_group(group_id)
    if group:
        service.delete_group(group_id)
        return None
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Group not found")