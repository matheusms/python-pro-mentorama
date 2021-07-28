from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

class Resp(BaseModel):
    curso: str
    modulo: int
    opt: Optional[str] = None
    tipo: str

@app.post("/novarota")
async def novarota(resp: Resp):
    return resp

#uvicorn aula_3:app --reload
