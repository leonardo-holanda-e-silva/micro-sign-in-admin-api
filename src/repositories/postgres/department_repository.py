import uuid
from typing import List, Any, Type, Optional

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from config.deps import get_pg_session
from src.models.department import Department


class DepartmentRepository:
    def __init__(self):
        self.session: AsyncSession = Depends(get_pg_session)

    def add(self, department: Department) -> None:
        self.session.add(department)
        self.session.commit()

    def get_by_id(self, department_id: uuid.UUID) -> Type[Department] | None:
        try:
            return self.session.query(Department).filter(Department.id == department_id).one()
        except NoResultFound:
            return None

    def get_all(self) -> List[Type[Department]]:
        return self.session.query(Department).all()

    def update(self, department: Type[Department]) -> Type[Department]:
        existing_department = self.get_by_id(department.id)
        if existing_department:
            existing_department.name = department.name
            existing_department.entry_date = department.entry_date
            existing_department.company = department.company
            existing_department.admins = department.admins
            existing_department.functions = department.functions
            self.session.commit()
            return existing_department

    def delete(self, department_id: uuid.UUID) -> None:
        department = self.get_by_id(department_id)
        if department:
            self.session.delete(department)
            self.session.commit()