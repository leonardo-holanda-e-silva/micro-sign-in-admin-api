from typing import List, Type
import uuid
from datetime import datetime
from src.models.department import Department
from src.repositories.postgres.department_repository import DepartmentRepository

class DepartmentService:
    def __init__(self, repository: DepartmentRepository):
        self.repository = repository

    def create_department(self, department: Department) -> Department:
        if department.entry_date is None:
            department.entry_date = datetime.utcnow()
        self.repository.add(department)
        return department

    def get_department(self, department_id: uuid.UUID) -> Type[Department] | None:
        return self.repository.get_by_id(department_id)

    def get_all_departments(self) -> List[Type[Department]]:
        return self.repository.get_all()

    def update_department(self, department: Department) -> None:
        existing_department = self.repository.get_by_id(department.id)
        if existing_department:
            existing_department.name = department.name
            existing_department.entry_date = department.entry_date
            existing_department.company = department.company
            existing_department.admins = department.admins
            existing_department.functions = department.functions
            self.repository.update(existing_department)

    def delete_department(self, department_id: uuid.UUID) -> None:
        self.repository.delete(department_id)
