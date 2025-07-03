# from datetime import datetime
# print("►►►HORA ACTUAL:",str(datetime.now()))

from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import os
import logging
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("api.log"),       # Log en archivo
        logging.StreamHandler()               # Log en consola
    ]
)

logger = logging.getLogger(__name__)

class User(BaseModel):
    id: int
    name: str

app = FastAPI()

@app.get("/")
def main():
    logger.info("GET/llamado"))
    return {"mesage":f"Hora actual: {str(datetime.now())}",
           "clave":os.getenv('clave','no encontro'),
           "msj":os.getenv('msj','no hay mensaje')}

@app.post("/user")
def user(user:User):
    logger.info(f"POST /user con datos: {user}")
    return user
