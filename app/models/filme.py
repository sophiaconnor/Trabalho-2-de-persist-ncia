
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.sessao import Sessao
    from app.models.genero import Genero

class Filme(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    sinopse: str
    duracao_minutos: int
    genero: list["Genero"] = Relationship(back_populates="filmes")
    classificacao: str
    sessoes: list["Sessao"] = Relationship(back_populates="filme")
  
