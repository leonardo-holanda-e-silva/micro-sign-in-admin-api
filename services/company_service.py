from typing import List, Type
import uuid
from datetime import datetime
from model.company import Company
from repositories.postgres.company_repository import CompanyRepository

class CompanyService:
    def __init__(self, repository: CompanyRepository):
        self.repository = repository

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
