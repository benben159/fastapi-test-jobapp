from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message","hello world"}

@app.get("/employees")
async def get_all_employee():
    pass

@app.get("/employees/{emp_id}")
async def get_employee(emp_id: int):
    pass

@app.post("/employees")
async def new_employee():
    pass

@app.put("/employees/{emp_id}")
async def update_employee(emp_id: int):
    pass
