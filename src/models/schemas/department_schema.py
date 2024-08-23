import uuid
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import List, Optional
from src.models.schemas.function_schema import FunctionSchema
from src.models.schemas.user_schema import UserSchema


class DepartmentSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    name: str
    entry_date: datetime = Field(default_factory=datetime.utcnow)
    company_id: Optional[UUID]
    admins: List[UserSchema]
    functions: List[FunctionSchema]

    class Config:
        orm_mode = True