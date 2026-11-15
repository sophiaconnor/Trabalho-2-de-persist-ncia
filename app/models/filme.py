
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.sessao import Sessao

from app.models.genero import Genero
from app.models.filme_genero import FilmeGenero

class Filme(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    sinopse: str
    generos: list["Genero"] = Relationship(
        back_populates="filmes",
        link_model=FilmeGenero
    )
    duracao_minutos: int
    
    classificacao: str
    sessoes: list["Sessao"] = Relationship(back_populates="filme")
  
