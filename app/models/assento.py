from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

from app.models.sessao import Sessao

if TYPE_CHECKING:
    from app.models.ingresso import Ingresso
    

class Assento(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    numero: int
    disponivel: bool = True

    ingresso: "Ingresso" | None = Relationship(
        back_populates="assento"
    )
    sessao: "Sessao" | None = Relationship(
        back_populates="assentos"
    )