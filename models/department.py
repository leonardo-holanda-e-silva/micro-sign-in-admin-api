import uuid

from company import Company
from datetime import datetime
from function import Function
from typing import List
from user import User

class Department:
    id:uuid
    name:str
    entry_date:datetime
    company:Company
    admins:List[User]
    functions:List[Function]