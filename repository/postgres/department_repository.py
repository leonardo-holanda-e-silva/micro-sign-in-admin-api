from repository.postgres.company_repository import CompanyRepository
from datetime import datetime
from repository.postgres.function_repository import FunctionRepository
from typing import List
from repository.postgres.user_repository import UserRepository

class DepartmentRepository:
    id:uuid
    name:str
    entry_date:datetime
    company:Company
    admins:List[User]
    functions:List[Function]