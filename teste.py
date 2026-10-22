
from sqlmodel import SQLModel

from app.models.filme import Filme
from app.models.sessao import Sessao

print(SQLModel.metadata.tables.keys())
print(Filme.__table__.columns.keys())
print(Sessao.__table__.columns.keys())
