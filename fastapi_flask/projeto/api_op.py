from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "API de operações matemáricas!(soma, subtracao, multiplicacao, divisao)"}

class Resp(BaseModel):
    valor1: int
    valor2: int
    operacao: str

@app.post("/operacao")
async def operacao(resp: Resp):
    if resp.operacao == "soma":
        return resp.valor1 + resp.valor2
    elif resp.operacao == "subtracao":
        return resp.valor1 - resp.valor2
    elif resp.operacao == "multiplicacao":
        return resp.valor1 * resp.valor2
    elif resp.operacao == "divisao":
        return resp.valor1 / resp.valor2

#uvicorn api_op:app --reload
