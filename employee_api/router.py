#from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from . import crud, models, schemas
from .config import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
emprouter = APIRouter()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@emprouter.get("/")
async def hello():
    return {"message":"hello world"}

@emprouter.get("/employees")
async def get_all_employee(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)) -> list[schemas.Employee]:
    empls = crud.get_employees(session, skip, limit)
    return [schemas.Employee.from_orm(e) for e in empls]

@emprouter.get("/employees/{emp_id}")
async def get_employee(emp_id: int, session: Session = Depends(get_db)) -> schemas.Employee:
    empl = crud.get_employee_by_id(session, emp_id)
    if empl is None:
        raise HTTPException(status_code=404, detail='employee not found')
    return schemas.Employee.from_orm(empl)

@emprouter.put("/employees")
async def new_employee(emp: schemas.EmployeeBase, session: Session = Depends(get_db)) -> schemas.Employee:
    empl = None
    try:
        empl = crud.create_employee(session, emp) 
    except IntegrityError as e:
        raise HTTPException(status_code=403, detail='email already registered')
    return schemas.Employee.from_orm(empl)

@emprouter.patch("/employees/{emp_id}")
async def update_employee(emp_id: int, emp: schemas.EmployeeUpdate, session: Session = Depends(get_db)):
    try:
        crud.update_employee(session, emp_id, emp)
    except IntegrityError as e:
        raise HTTPException(status_code=403, detail='email already registered')

@emprouter.delete("/employees/{emp_id}")
async def delete_employee(emp_id: int, session: Session = Depends(get_db)):
    empl = crud.get_employee_by_id(session, emp_id)
    if empl is None:
        raise HTTPException(status_code=404, detail='employee not found')
    session.delete(empl)
    session.commit()
