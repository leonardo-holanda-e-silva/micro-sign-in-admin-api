import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from config.configs import settings
from datetime import datetime

class Permission(settings.DBBaseModel):
    __tablename__ = 'permission'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    entry_date = Column(DateTime, default=datetime.utcnow)
