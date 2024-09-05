import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.configs import settings
from datetime import datetime

company_admins = Table(
    'company_admins', settings.DBBaseModel.metadata,
    Column('company_id', UUID(as_uuid=True), ForeignKey('company.id'), primary_key=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True)
)

company_departments = Table(
    'company_departments', settings.DBBaseModel.metadata,
    Column('company_id', UUID(as_uuid=True), ForeignKey('company.id'), primary_key=True),
    Column('department_id', UUID(as_uuid=True), ForeignKey('department.id'), primary_key=True)
)


class Company(settings.DBBaseModel):
    __tablename__ = 'company'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    entry_date = Column(DateTime, default=datetime.now())

    admins = relationship('User', secondary=company_admins, back_populates='companies')
    departments = relationship('Department', secondary=company_departments, back_populates='companies')
