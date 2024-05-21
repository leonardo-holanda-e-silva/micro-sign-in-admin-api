import uuid

from company import Company
from datetime import date
from datetime import datetime
from department import Department
from function import Function
from group import Group
from typing import Dict, List

class User:
    id:uuid
    name:str
    mails:Dict[str,str]
    adresses:Dict[str,str]
    birth:date
    entry_date:datetime
    phones:Dict[str,str]
    companies:List[Company]
    departments:List[Department]
    functions:List[Function]
    groups:List[Group]