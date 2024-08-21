from typing import List, Type
import uuid
from datetime import datetime
from model.function import Function
from repository.postgres.function_repository import FunctionRepository

class FunctionService:
    def __init__(self, repository: FunctionRepository):
        self.repository = repository

    def create_function(self, function: Function) -> Function:
        if function.entry_date is None:
            function.entry_date = datetime.utcnow()
        self.repository.add(function)
        return function

    def get_function(self, function_id: uuid.UUID) -> Type[Function] | None:
        return self.repository.get_by_id(function_id)

    def get_all_functions(self) -> List[Type[Function]]:
        return self.repository.get_all()

    def update_function(self, function: Function) -> None:
        existing_function = self.repository.get_by_id(function.id)
        if existing_function:
            existing_function.name = function.name
            existing_function.entry_date = function.entry_date
            self.repository.update(existing_function)

    def delete_function(self, function_id: uuid.UUID) -> None:
        self.repository.delete(function_id)
