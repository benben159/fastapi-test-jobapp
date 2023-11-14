from sqlalchemy.orm import Session

from . import models, schemas

def create_employee(db: Session, emp: schemas.EmployeeBase):
    db_emp = models.Employee(first_name=emp.first_name, last_name=emp.last_name, email=emp.email)
    db.add(db_emp)
    return db_emp

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def get_employee_by_id(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()

def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()

def update_employee(db: Session, emp_id: int, emp_update: schemas.EmployeeUpdate):
    db_emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    db_emp.first_name = emp_update.first_name 
    db_emp.last_name = emp_update.last_name
    db_emp.email = emp_update.email
    # FIXME return false if update fail
    db_emp.save()
