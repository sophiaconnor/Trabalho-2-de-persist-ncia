from sqlmodel import SQLModel, Session, create_engine
import app.models

DATABASE_URL = "sqlite:///teste.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)


def criar_tabelas():
    SQLModel.metadata.create_all(engine)


def obter_sessao():
    with Session(engine) as session:
        yield session