from typing import List, Optional

from pydantic import BaseModel

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]
    meus_produtos: List[Produtos]

class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    usuario: Usuario
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




