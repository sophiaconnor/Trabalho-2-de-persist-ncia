from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import obter_sessao
from app.services.sessao_service import listar_sessoes_por_filme

router = APIRouter(prefix="/sessoes", tags=["Sessões"])


@router.get("/filme/{titulo}")
def consultar_sessoes_por_filme(
    titulo: str,
    session: Session = Depends(obter_sessao)
):
    return listar_sessoes_por_filme(session, titulo)