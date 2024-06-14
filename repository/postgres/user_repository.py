from repository.postgres.company_repository import CompanyRepository
from repository.postgres.department_repository import DepartmentRepository
from repository.postgres.function_repository import FunctionRepository
from repository.postgres.group_repository import GroupRepository
from typing import Dict, List

class UserRepository:
    id:uuid
    name:str
    mails:Dict[str,str]
    adresses:Dict[str,str]
    birth:date
    entry_date:datetime
    phones:Dict[str,str]
    companies:List[CompanyRepository]
    departments:List[DepartmentRepository]
    functions:List[FunctionRepository]
    groups:List[GroupRepository]