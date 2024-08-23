from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
import uuid

class PermissionSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    name: str
    entry_date: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
