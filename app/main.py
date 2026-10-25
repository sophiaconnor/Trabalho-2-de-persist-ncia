from contextlib import asynccontextmanager
from app.routers import filmes
from fastapi import FastAPI

from app.database import criar_tabelas

#permite definir o que acontece durante o ciclo de vida da aplicação
@asynccontextmanager

async def lifespan(app: FastAPI):
    criar_tabelas()
    #indica que o código após o yield será executado quando a aplicação for encerrada
    yield

app = FastAPI(
    title="Sistema de Cinema",
    description="API para gerenciamento de um sistema de cinema",
    version="1.0.0",
    lifespan=lifespan
)