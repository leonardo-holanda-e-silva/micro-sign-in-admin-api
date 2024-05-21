import uuid

from department import Department 
from datetime import datetime
from typing import List
from user import User

class Company:
    id:uuid
    name:str
    entry_date:datetime
    admins:List[User]
    departments:List[Department]