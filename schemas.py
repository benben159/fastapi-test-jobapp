from typing import List, Union

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
	email: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
