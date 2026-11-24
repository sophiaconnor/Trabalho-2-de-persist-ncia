from sqlmodel import SQLModel, Session, create_engine
import app.models
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///teste.db"
)

connect_args = {}

if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)


def criar_tabelas():
    SQLModel.metadata.create_all(engine)


def obter_sessao():
    with Session(engine) as session:
        yield session


def obter_ingresso():
    with Session(engine) as session:
        yield session