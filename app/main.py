from fastapi import FastAPI, HTTPException
from typing import List
from app.schema import Item
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Simualação de um banco de dados
banco: List[Item] = []

@app.get("/", status_code=200)
async def listando_produto():
  if not banco:
    raise HTTPException(status_code=404, detail="Não tem produto registrado!")
  return banco

@app.get("/{produto_id}", status_code=200)
async def getid(produto_id: str):
  for produto in banco:
    if produto.id == produto_id:
      return produto
  raise HTTPException(status_code=404, detail="Produto não encontrado nesse id")

@app.post("/", status_code=201)
async def criando_produto(produto: Item):
  produto.id = str(uuid4())
  banco.append(produto)
  return {"message": "Produto criado com sucesso!"}

@app.put("/")
async def editando_produto(produto: Item):
  return banco
  
@app.delete("/{produto_id}", status_code=200)
async def apagar_produto(produto_id: str):
  posicao = -1
  for index, produto in enumerate(banco):
    if produto.id == produto_id:
      posicao = index
      break
  if posicao != -1:
    banco.pop(posicao)
    return {"message": "Produto deletado com sucesso!"}
  else:
    raise HTTPException(status_code=404, detail="Produto não encontrado nesse id")