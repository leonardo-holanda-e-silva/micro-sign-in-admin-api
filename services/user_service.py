from typing import List, Type
import uuid
from datetime import datetime
from model.user import User
from repositories.postgres.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: User) -> User:
        if user.entry_date is None:
            user.entry_date = datetime.utcnow()
        self.repository.add(user)
        return user

    def get_user(self, user_id: uuid.UUID) -> Type[User] | None:
        return self.repository.get_by_id(user_id)

    def get_all_users(self) -> List[Type[User]]:
        return self.repository.get_all()

    def update_user(self, user: User) -> None:
        existing_user = self.repository.get_by_id(user.id)
        if existing_user:
            existing_user.name = user.name
            existing_user.mails = user.mails
            existing_user.addresses = user.addresses
            existing_user.birth = user.birth
            existing_user.entry_date = user.entry_date
            existing_user.phones = user.phones
            self.repository.update(existing_user)

    def delete_user(self, user_id: uuid.UUID) -> None:
        self.repository.delete(user_id)
