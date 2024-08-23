import uuid
from typing import List, Any, Type, Optional

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.models.department import Department


class DepartmentRepository:
    def __init__(self, session: Session):
        self.session = session

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

    def update(self, department: Department) -> None:
        existing_department = self.get_by_id(department.id)
        if existing_department:
            existing_department.name = department.name
            existing_department.entry_date = department.entry_date
            existing_department.company = department.company
            existing_department.admins = department.admins
            existing_department.functions = department.functions
            self.session.commit()

    def delete(self, department_id: uuid.UUID) -> None:
        department = self.get_by_id(department_id)
        if department:
            self.session.delete(department)
            self.session.commit()