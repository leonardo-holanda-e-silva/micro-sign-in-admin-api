from pydantic import BaseModel, Field, EmailStr, constr, field_validator
from uuid import UUID
import uuid
import re

class UserRegistrySchema(BaseModel):
    key: UUID = Field(default_factory=uuid.uuid4)
    name: constr(max_length=100) = Field(...)
    department: constr(max_length=100) = Field(...)
    role: constr(max_length=50) = Field(...)
    password: str = Field(...)
    email: EmailStr = Field(...)
    phone: constr(max_length=15) = Field(...)
    photo: str = Field(...)
    active: bool = Field(default=True)

    @field_validator('password')
    @staticmethod  # Torna o método estático
    def validate_password(value):
        if not re.search(r'[a-z]', value):
            raise ValueError('Password must contain at least one lowercase letter.')
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not re.search(r'\d', value):
            raise ValueError('Password must contain at least one number.')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError('Password must contain at least one special character.')
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        return value
