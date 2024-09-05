import uuid
from typing import List, Type

from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from src.services.permission_service import PermissionService as Service
from src.models.permission import Permission
from src.models.schemas.permission_schema import PermissionSchema as Schema

service = Service()
router = APIRouter()

@router.post("/permission", status_code=HTTP_201_CREATED)
async def create_permission(schema: Schema):
    permission = Permission()
    permission.name = schema.name
    return service.create_permission(permission)

@router.get("/permission/{permission_id}", response_model=Permission)
async def get_permission(permission_id: uuid) -> Type[Permission] | None:
    permission = service.get_permission(permission_id)
    if Permission:
        return permission
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Permission not found")

@router.get("/permissions", response_model=List[Permission])
async def list_permissions() -> list[Type[Permission]]:
    permissions = service.get_all_permissions()
    return permissions

@router.put("/permission/{permission_id}", response_model=Permission)
async def update_permission(permission_id: uuid, schema: Schema) -> Type[Permission]:
    permission = service.get_permission(permission_id)
    if permission:
        permission.name = schema.name
        return service.update_permission(permission)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Permission not found")

@router.delete("/permission/{permission_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_permission(permission_id: uuid):
    permission = service.get_permission(permission_id)
    if permission:
        service.delete_permission(permission_id)
        return None
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Permission not found")