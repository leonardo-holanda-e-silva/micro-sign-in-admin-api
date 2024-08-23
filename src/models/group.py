import uuid
from sqlalchemy import Column, String, DateTime, Table, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config.configs import settings
from datetime import datetime

group_permissions = Table(
    'group_permissions', settings.DBBaseModel.metadata,
    Column('group_id', UUID(as_uuid=True), ForeignKey('group.id'), primary_key=True),
    Column('permission_id', UUID(as_uuid=True), ForeignKey('permission.id'), primary_key=True)
)

group_users = Table(
    'group_users', settings.DBBaseModel.metadata,
    Column('group_id', UUID(as_uuid=True), ForeignKey('group.id'), primary_key=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True)
)

group_systems = Table(
    'group_systems', settings.DBBaseModel.metadata,
    Column('group_id', UUID(as_uuid=True), ForeignKey('group.id'), primary_key=True),
    Column('system_id', UUID(as_uuid=True), ForeignKey('system.id'), primary_key=True)
)


class Group(settings.DBBaseModel):
    __tablename__ = 'group'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    entry_date = Column(DateTime, default=datetime.utcnow)

    permissions = relationship('Permission', secondary=group_permissions, back_populates='groups')
    users = relationship('User', secondary=group_users, back_populates='groups')
    systems = relationship('System', secondary=group_systems, back_populates='groups')