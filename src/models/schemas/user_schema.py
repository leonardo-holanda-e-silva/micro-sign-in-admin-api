from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, date
from typing import List, Dict, Optional
import uuid

class UserSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    name: str
    mails: Dict[str, str]
    addresses: Dict[str, str]
    birth: date
    entry_date: datetime = Field(default_factory=datetime.utcnow)
    phones: Dict[str, str]

    class Config:
        orm_mode = True