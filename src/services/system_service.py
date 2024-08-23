from typing import List, Type
import uuid
from datetime import datetime
from src.models.system import System
from src.repositories.postgres.system_repository import SystemRepository

class SystemService:
    def __init__(self, repository: SystemRepository):
        self.repository = repository

    def create_system(self, system: System) -> System:
        if system.entry_date is None:
            system.entry_date = datetime.utcnow()
        self.repository.add(system)
        return system

    def get_system(self, system_id: uuid.UUID) -> Type[System] | None:
        return self.repository.get_by_id(system_id)

    def get_all_systems(self) -> List[Type[System]]:
        return self.repository.get_all()

    def update_system(self, system: System) -> None:
        existing_system = self.repository.get_by_id(system.id)
        if existing_system:
            existing_system.name = system.name
            existing_system.entry_date = system.entry_date
            existing_system.url = system.url
            self.repository.update(existing_system)

    def delete_system(self, system_id: uuid.UUID) -> None:
        self.repository.delete(system_id)
