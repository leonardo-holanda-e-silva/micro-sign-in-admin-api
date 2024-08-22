from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import List, Optional
import uuid

from models.schemas.permission_schema import PermissionSchema
from models.schemas.system_schema import SystemSchema
from models.schemas.user_schema import UserSchema


class GroupBase(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    name: str
    entry_date: datetime = Field(default_factory=datetime.utcnow)
    systems: List[SystemSchema]
    permissions: List[PermissionSchema]
    users: List[UserSchema]

    class Config:
        orm_mode = True