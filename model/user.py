import uuid
from sqlalchemy import Column, String, Date, DateTime, Table, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

user_companies = Table(
    'user_companies', Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True),
    Column('company_id', UUID(as_uuid=True), ForeignKey('company.id'), primary_key=True)
)

user_departments = Table(
    'user_departments', Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True),
    Column('department_id', UUID(as_uuid=True), ForeignKey('department.id'), primary_key=True)
)

user_functions = Table(
    'user_functions', Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True),
    Column('function_id', UUID(as_uuid=True), ForeignKey('function.id'), primary_key=True)
)

user_groups = Table(
    'user_groups', Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True),
    Column('group_id', UUID(as_uuid=True), ForeignKey('group.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    mails = Column(JSONB, nullable=False)
    addresses = Column(JSONB, nullable=False)
    birth = Column(Date, nullable=False)
    entry_date = Column(DateTime, default=datetime.utcnow)
    phones = Column(JSONB, nullable=False)

    companies = relationship('Company', secondary=user_companies, back_populates='users')
    departments = relationship('Department', secondary=user_departments, back_populates='users')
    functions = relationship('Function', secondary=user_functions, back_populates='users')
    groups = relationship('Group', secondary=user_groups, back_populates='users')
