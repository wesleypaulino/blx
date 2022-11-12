from typing import List, Optional

from pydantic import BaseModel


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    # meus_produtos: List[Produto]
    # minhas_vendas: List[Pedido]
    # meus_pedidos: List[Pedido]

    # Transformar automaticamente em Schema
    class Config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
