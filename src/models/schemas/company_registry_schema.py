from pydantic import BaseModel, Field, constr, EmailStr, AnyUrl
from uuid import UUID
import uuid

class CompanyRegistrySchema(BaseModel):
    key: UUID = Field(default_factory=uuid.uuid4)
    name: constr(max_length=100) = Field(...)
    logo: str = Field(...)
    website: AnyUrl = Field(...)
    size: int = Field(gt=0)
    active: bool = Field(default=True)
