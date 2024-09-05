from typing import List
import uuid
from datetime import datetime

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.company import Company
from src.models.department import Department
from src.repositories.postgres.company_repository import CompanyRepository as Respository

class CompanyService:
    def __init__(self):
        self.repository = Respository()

    def create_company(self, company: Company) -> Company:
        if company.entry_date is None:
            company.entry_date = datetime.utcnow()
        self.repository.add(company)
        return company

    def get_company(self, company_id: uuid.UUID) -> Company:
        return self.repository.get_by_id(company_id)

    def get_all_companies(self) -> List[Company]:
        return self.repository.get_all()

    def update_company(self, company: Company) -> None:
        existing_company = self.repository.get_by_id(company.id)
        if existing_company:
            existing_company.name = company.name
            existing_company.entry_date = company.entry_date
            existing_company.admins = company.admins
            existing_company.departments = company.departments
            self.repository.update(existing_company)

    def delete_company(self, company_id: uuid.UUID) -> None:
        self.repository.delete(company_id)
