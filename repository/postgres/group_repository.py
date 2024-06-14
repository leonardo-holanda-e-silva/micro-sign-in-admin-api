from datetime import datetime
from repository.postgres.permission_repository import PermissionRepository
from typing import List
from repository.postgres.user_repository import UserRepository

class GroupRepository:
    id:uuid
    name:str
    entry_date:datetime
    permissions:List[PermissionRepository]
    users:List[UserRepository]
    systems:List