from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List, Type, Any
import uuid

from models.function import Function


class FunctionRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, function: Function) -> None:
        self.session.add(function)
        self.session.commit()

    def get_by_id(self, function_id: uuid.UUID) -> Type[Function] | None:
        try:
            return self.session.query(Function).filter(Function.id == function_id).one()
        except NoResultFound:
            return None

    def get_all(self) -> List[Type[Function]]:
        return self.session.query(Function).all()

    def update(self, function: Function) -> None:
        existing_function = self.get_by_id(function.id)
        if existing_function:
            existing_function.name = function.name
            existing_function.entry_date = function.entry_date
            self.session.commit()

    def delete(self, function_id: uuid.UUID) -> None:
        function = self.get_by_id(function_id)
        if function:
            self.session.delete(function)
            self.session.commit()
