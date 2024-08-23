import uuid
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class SystemSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    name: str
    entry_date: datetime = Field(default_factory=datetime.utcnow)
    url: str

    class Config:
        orm_mode = True
