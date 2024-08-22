import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.configs import settings
from datetime import datetime

department_admins = Table(
    'department_admins', settings.DBBaseModel.metadata,
    Column('department_id', UUID(as_uuid=True), ForeignKey('department.id'), primary_key=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True)
)

department_functions = Table(
    'department_functions', settings.DBBaseModel.metadata,
    Column('department_id', UUID(as_uuid=True), ForeignKey('department.id'), primary_key=True),
    Column('function_id', UUID(as_uuid=True), ForeignKey('function.id'), primary_key=True)
)


class Department(settings.DBBaseModel):
    __tablename__ = 'department'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    entry_date = Column(DateTime, default=datetime.utcnow)

    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'))
    company = relationship('Company', back_populates='departments')

    admins = relationship('User', secondary=department_admins, back_populates='departments')
    functions = relationship('Function', secondary=department_functions, back_populates='departments')
