from typing import List, Union, Optional

from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
