
from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.filme import Filme
    from app.models.sala import Sala
    from app.models.ingresso import Ingresso


class Sessao(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    data_hora: datetime
    preco: float
    filme_id: int = Field(foreign_key="filme.id")
    sala_id: int = Field(foreign_key="sala.id")

    sala: "Sala" = Relationship(back_populates="sessoes")
    filme: "Filme" = Relationship(back_populates="sessoes")
    ingressos: list["Ingresso"] = Relationship(back_populates="sessao")
