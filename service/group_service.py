from typing import List, Type
import uuid
from datetime import datetime
from model.group import Group
from repository.postgres.group_repository import GroupRepository

class GroupService:
    def __init__(self, repository: GroupRepository):
        self.repository = repository

    def create_group(self, group: Group) -> Group:
        if group.entry_date is None:
            group.entry_date = datetime.utcnow()
        self.repository.add(group)
        return group

    def get_group(self, group_id: uuid.UUID) -> Type[Group] | None:
        return self.repository.get_by_id(group_id)

    def get_all_groups(self) -> List[Type[Group]]:
        return self.repository.get_all()

    def update_group(self, group: Group) -> None:
        existing_group = self.repository.get_by_id(group.id)
        if existing_group:
            existing_group.name = group.name
            existing_group.entry_date = group.entry_date
            existing_group.permissions = group.permissions
            existing_group.users = group.users
            existing_group.systems = group.systems
            self.repository.update(existing_group)

    def delete_group(self, group_id: uuid.UUID) -> None:
        self.repository.delete(group_id)
