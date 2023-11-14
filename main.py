from fastapi import FastAPI
from employee_api.router import emprouter

app = FastAPI()
app.include_router(emprouter)
