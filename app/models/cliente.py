from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel
from datetime import date

if TYPE_CHECKING:
    from app.models.ingresso import Ingresso


class Cliente(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str
    data_nascimento: date | None = None

    ingressos: list["Ingresso"] = Relationship(
        back_populates="cliente"
    )
