
from typing import TYPE_CHECKING

from sqlmodel import Field, SQLModel
if TYPE_CHECKING:
    from app.models.filme import Filme
    from app.models.genero import Genero


class FilmeGenero(SQLModel, table=True):
    filme_id: int = Field(
        foreign_key="filme.id",
        primary_key=True
    )

    genero_id: int = Field(
        foreign_key="genero.id",
        primary_key=True
    )
