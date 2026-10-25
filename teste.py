print("INÍCIO DO TESTE")

from sqlmodel import SQLModel
from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import configure_mappers
from app.models.filme import Filme
from app.models.sala import Sala
from app.models.sessao import Sessao
from app.models.cliente import Cliente
from app.models.ingresso import Ingresso
from app.models.validacao import Validacao

print("Modelos importados!")

engine = create_engine("sqlite:///teste.db", echo=True)

print("Criando as tabelas...")

SQLModel.metadata.create_all(engine)

print("Tabelas criadas com sucesso!")

print("Configurando os relacionamentos...")
SQLModel.metadata.tables

print("Tabelas registradas:")
for nome_tabela in SQLModel.metadata.tables:
    print(nome_tabela)

print("Verificando relacionamentos...")
configure_mappers()
print("Relacionamentos configurados!")
print("TESTE CONCLUÍDO!")