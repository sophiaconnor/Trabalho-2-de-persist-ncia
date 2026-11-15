from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

from app.models.sessao import Sessao

if TYPE_CHECKING:
    from app.models.ingresso import Ingresso
    from app.models.sala import Sala
    

class Assento(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    identificacao: str = Field
    disponivel: bool = True
    sala_id: int | None = Field(default=None, foreign_key="sala.id")
    ingressos: list["Ingresso"] | None = Relationship(
        back_populates="assento"
    )
    sala: "Sala" | None = Relationship(
        back_populates="assentos"
    )