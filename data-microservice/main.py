from fastapi import FastAPI

from src import method

app = FastAPI()

app.include_router(method.router)




