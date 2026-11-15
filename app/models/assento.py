from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

from app.models.sessao import Sessao

if TYPE_CHECKING:
    from app.models.ingresso import Ingresso
    from app.models.sala import Sala
    

class Assento(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    identificacao: str = Field
    sala_id: int = Field(default=None, foreign_key="sala.id")
    ingressos: list["Ingresso"] | None = Relationship(
        back_populates="assento"
    )
    sala: "Sala" = Relationship(
        back_populates="assentos"
    )