from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.sala import Sala
    from app.models.validacao import Validacao

from app.models.cliente import Cliente
from app.models.sessao import Sessao

class Ingresso(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id")
    sessao_id: int = Field(foreign_key="sessao.id")
    preco: float
    validacao: "Validacao" = Relationship(back_populates="ingresso")

    cliente: Cliente = Relationship(back_populates="ingressos")
    sessao: Sessao = Relationship(back_populates="ingressos")