import uuid
from typing import List, Type

from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from src.services.department_service import DepartmentService as Service
from src.models.department import Department
from src.models.schemas.department_schema import DepartmentSchema as Schema

service = Service()
router = APIRouter()

@router.post("/department", status_code=HTTP_201_CREATED)
async def create_department(schema: Schema):
    department = Department()
    department.name = schema.name
    return service.create_department(department)

@router.get("/department/{department_id}", response_model=Department)
async def get_department(department_id: uuid) -> Type[Department] | None:
    department = service.get_department(department_id)
    if Department:
        return department
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Department not found")

@router.get("/departments", response_model=List[Department])
async def list_departments() -> list[Type[Department]]:
    departments = service.get_all_departments()
    return departments

@router.put("/department/{department_id}", response_model=Department)
async def update_department(department_id: uuid, schema: Schema) -> Type[Department]:
    department = service.get_department(department_id)
    if department:
        department.name = schema.name
        return service.update_department(department)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Department not found")

@router.delete("/department/{department_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_department(department_id: uuid):
    department = service.get_department(department_id)
    if department:
        service.delete_department(department_id)
        return None
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Department not found")