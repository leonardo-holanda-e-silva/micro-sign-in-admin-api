from pydantic import BaseModel, Field, constr, EmailStr
from uuid import UUID
from datetime import datetime
import uuid

class RegistrySchema(BaseModel):
    user_name: constr(max_length=100) = Field(..., description="100 char user name.")
    email: EmailStr = Field(..., description="Valid Email Address.")
    company_name: constr(max_length=100) = Field(..., description="Company name, up to 100 characters.")
