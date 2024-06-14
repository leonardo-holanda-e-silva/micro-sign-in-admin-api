from repository.postgres.department_repository import DepartmentRepository
from typing import List, Optional
from repository.postgres.user_repository import UserRepository

from sqlalchemy import ForeignKey, String, UUID, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class CompanyRepository(Base):
    __tablename__ = "Company"

    id:Mapped[UUID] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    entry_date:Mapped[TIMESTAMP]
    admins:Mapped[List[UserRepository]]
    departments:Mapped[List[DepartmentRepository]]