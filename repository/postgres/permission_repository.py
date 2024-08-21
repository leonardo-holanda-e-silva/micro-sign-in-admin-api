from model.permission import Permission
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List, Type
import uuid

class PermissionRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, permission: Permission) -> None:
        self.session.add(permission)
        self.session.commit()

    def get_by_id(self, permission_id: uuid.UUID) -> Type[Permission] | None:
        try:
            return self.session.query(Permission).filter(Permission.id == permission_id).one()
        except NoResultFound:
            return None

    def get_all(self) -> List[Type[Permission]]:
        return self.session.query(Permission).all()

    def update(self, permission: Permission) -> None:
        existing_permission = self.get_by_id(permission.id)
        if existing_permission:
            existing_permission.name = permission.name
            existing_permission.entry_date = permission.entry_date
            self.session.commit()

    def delete(self, permission_id: uuid.UUID) -> None:
        permission = self.get_by_id(permission_id)
        if permission:
            self.session.delete(permission)
            self.session.commit()
