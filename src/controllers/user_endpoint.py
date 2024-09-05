import uuid
from typing import List, Type

from fastapi import APIRouter, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from src.services.user_service import UserService as Service
from src.models.user import User
from src.models.schemas.user_schema import UserSchema as Schema

service = Service()
router = APIRouter()

@router.post("/user", status_code=HTTP_201_CREATED)
async def create_user(schema: Schema):
    user = User()
    user.name = schema.name
    return service.create_user(user)

@router.get("/user/{user_id}", response_model=User)
async def get_user(user_id: uuid) -> Type[User] | None:
    user = service.get_user(user_id)
    if User:
        return user
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

@router.get("/users", response_model=List[User])
async def list_users() -> list[Type[User]]:
    users = service.get_all_users()
    return users

@router.put("/user/{user_id}", response_model=User)
async def update_user(user_id: uuid, schema: Schema) -> Type[User]:
    user = service.get_user(user_id)
    if user:
        user.name = schema.name
        return service.update_user(user)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

@router.delete("/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_user(user_id: uuid):
    user = service.get_user(user_id)
    if user:
        service.delete_user(user_id)
        return None
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")