from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.sessao import Sessao
    from app.models.ingresso import Ingresso

class Sala(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    numero: int
    capacidade: int
    tipo: str
    #garante que cada sala tenha uma lista de sessões associadas a ela
    sessoes: list["Sessao"] = Relationship(back_populates="sala")
    capacidade: int