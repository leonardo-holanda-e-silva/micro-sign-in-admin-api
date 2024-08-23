from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List, Type
import uuid

from src.models.system import System


class SystemRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, system: System) -> None:
        self.session.add(system)
        self.session.commit()

    def get_by_id(self, system_id: uuid.UUID) -> Type[System] | None:
        try:
            return self.session.query(System).filter(System.id == system_id).one()
        except NoResultFound:
            return None

    def get_all(self) -> List[Type[System]]:
        return self.session.query(System).all()

    def update(self, system: System) -> None:
        existing_system = self.get_by_id(system.id)
        if existing_system:
            existing_system.name = system.name
            existing_system.entry_date = system.entry_date
            existing_system.url = system.url
            self.session.commit()

    def delete(self, system_id: uuid.UUID) -> None:
        system = self.get_by_id(system_id)
        if system:
            self.session.delete(system)
            self.session.commit()
