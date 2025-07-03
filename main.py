# from datetime import datetime
# print("►►►HORA ACTUAL:",str(datetime.now()))

from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv()

class User(BaseModel):
    id: int
    name: str

app = FastAPI()

@app.get("/")
def main():
    return {"mesage":f"Hora actual: {str(datetime.now())}",
           "clave":os.getenv('clave','no encontro')}

@app.post("/user")
def user(user:User):
    return user
