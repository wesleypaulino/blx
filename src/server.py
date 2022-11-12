from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositoryProduto

criar_bd()

app = FastAPI()


@app.get('/produtos')
def listar_produtos():
    return {'msg': 'listagem de produtos'}


@app.post('/produtos')
# Passa Schema do Produto, Abre Conexao com Banco, Injeta Dependenica para obter a função get_db
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositoryProduto().criar(produto)
    return {produto_criado}
