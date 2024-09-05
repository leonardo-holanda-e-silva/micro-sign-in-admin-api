import uuid
from typing import List, Type

from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from src.services.function_service import FunctionService as Service
from src.models.function import Function
from src.models.schemas.function_schema import FunctionSchema as Schema

service = Service()
router = APIRouter()

@router.post("/function", status_code=HTTP_201_CREATED)
async def create_function(schema: Schema):
    function = Function()
    function.name = schema.name
    return service.create_function(function)

@router.get("/function/{function_id}", response_model=Function)
async def get_function(function_id: uuid) -> Type[Function] | None:
    function = service.get_function(function_id)
    if Function:
        return function
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Function not found")

@router.get("/functions", response_model=List[Function])
async def list_functions() -> list[Type[Function]]:
    functions = service.get_all_functions()
    return functions

@router.put("/function/{function_id}", response_model=Function)
async def update_function(function_id: uuid, schema: Schema) -> Type[Function]:
    function = service.get_function(function_id)
    if function:
        function.name = schema.name
        return service.update_function(function)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Function not found")

@router.delete("/function/{function_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_function(function_id: uuid):
    function = service.get_function(function_id)
    if function:
        service.delete_function(function_id)
        return None
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Function not found")