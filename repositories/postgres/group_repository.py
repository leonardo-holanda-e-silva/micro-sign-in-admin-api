from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List, Any, Type
import uuid

from model.group import Group


class GroupRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, group: Group) -> None:
        self.session.add(group)
        self.session.commit()

    def get_by_id(self, group_id: uuid.UUID) -> Type[Group] | None:
        try:
            return self.session.query(Group).filter(Group.id == group_id).one()
        except NoResultFound:
            return None

    def get_all(self) -> List[Type[Group]]:
        return self.session.query(Group).all()

    def update(self, group: Group) -> None:
        existing_group = self.get_by_id(group.id)
        if existing_group:
            existing_group.name = group.name
            existing_group.entry_date = group.entry_date
            existing_group.permissions = group.permissions
            existing_group.users = group.users
            existing_group.systems = group.systems
            self.session.commit()

    def delete(self, group_id: uuid.UUID) -> None:
        group = self.get_by_id(group_id)
        if group:
            self.session.delete(group)
            self.session.commit()
