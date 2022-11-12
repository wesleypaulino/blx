from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

# Representa os dados no banco de dados


class RepositoryProduto():

    def __init__(self, db: Session):
        self.db = db

    # Schemas usado somente Request Response
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel)

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def obter(self) -> None:
        pass

    def remover(self) -> None:
        pass
