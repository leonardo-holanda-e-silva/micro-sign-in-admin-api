import uuid
from typing import List, Any, Type

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from src.models.company import Company

class CompanyRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, company: Company) -> None:
        self.session.add(company)
        self.session.commit()

    def get_by_id(self, company_id: uuid.UUID) -> Type[Company] | None:
        try:
            return self.session.query(Company).filter(Company.id == company_id).one()
        except NoResultFound:
            return None

    def get_all(self) -> List[Type[Company]]:
        return self.session.query(Company).all()

    def update(self, company: Company) -> None:
        existing_company = self.get_by_id(company.id)
        if existing_company:
            existing_company.name = company.name
            existing_company.entry_date = company.entry_date
            existing_company.admins = company.admins
            existing_company.departments = company.departments
            self.session.commit()

    def delete(self, company_id: uuid.UUID) -> None:
        company = self.get_by_id(company_id)
        if company:
            self.session.delete(company)
            self.session.commit()