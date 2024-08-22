from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List, Type
import uuid

from model.user import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: User) -> None:
        self.session.add(user)
        self.session.commit()

    def get_by_id(self, user_id: uuid.UUID) -> Type[User] | None:
        try:
            return self.session.query(User).filter(User.id == user_id).one()
        except NoResultFound:
            return None

    def get_all(self) -> List[Type[User]]:
        return self.session.query(User).all()

    def update(self, user: User) -> None:
        existing_user = self.get_by_id(user.id)
        if existing_user:
            existing_user.name = user.name
            existing_user.mails = user.mails
            existing_user.addresses = user.addresses
            existing_user.birth = user.birth
            existing_user.entry_date = user.entry_date
            existing_user.phones = user.phones
            existing_user.companies = user.companies
            existing_user.departments = user.departments
            existing_user.functions = user.functions
            existing_user.groups = user.groups
            self.session.commit()

    def delete(self, user_id: uuid.UUID) -> None:
        user = self.get_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
