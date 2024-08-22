from typing import List
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from models.schemas.user_schema import UserSchema
from models.schemas.department_schema import DepartmentSchema
import uuid

class CompanySchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    name: str
    entry_date: datetime = Field(default_factory=datetime.utcnow)
    admins: List[UserSchema]
    departments: List[DepartmentSchema]

    class Config:
        orm_mode = True