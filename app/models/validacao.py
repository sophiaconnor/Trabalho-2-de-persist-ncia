from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

if TYPE_CHECKING:
    from app.models.ingresso import Ingresso


class Validacao(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("ingresso_id"),
    )

    id: int | None = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    ingresso_id: int = Field(foreign_key="ingresso.id")

    ingresso: "Ingresso" = Relationship(back_populates="validacao")