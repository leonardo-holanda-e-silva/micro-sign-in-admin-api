import uuid

from datetime import datetime
from permission import Permission
from typing import List
from user import User

class Group:
    id:uuid
    name:str
    entry_date:datetime
    permissions:List[Permission]
    users:List[User]
    systems:List