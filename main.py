from fastapi import FastAPI
from .router import emprouter

app = FastAPI()
app.include_router(emprouter)
