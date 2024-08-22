from typing import List, Type
import uuid
from datetime import datetime
from model.permission import Permission
from repositories.postgres.permission_repository import PermissionRepository

class PermissionService:
    def __init__(self, repository: PermissionRepository):
        self.repository = repository

    def create_permission(self, permission: Permission) -> Permission:
        if permission.entry_date is None:
            permission.entry_date = datetime.utcnow()
        self.repository.add(permission)
        return permission

    def get_permission(self, permission_id: uuid.UUID) -> Type[Permission] | None:
        return self.repository.get_by_id(permission_id)

    def get_all_permissions(self) -> List[Type[Permission]]:
        return self.repository.get_all()

    def update_permission(self, permission: Permission) -> None:
        existing_permission = self.repository.get_by_id(permission.id)
        if existing_permission:
            existing_permission.name = permission.name
            existing_permission.entry_date = permission.entry_date
            self.repository.update(existing_permission)

    def delete_permission(self, permission_id: uuid.UUID) -> None:
        self.repository.delete(permission_id)
