from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import obter_sessao
from app.services.sessao_service import listar_sessoes_por_filme

router = APIRouter(prefix="/sessoes", tags=["Sessões"])


@router.get("/filme/{filme_id}")
def consultar_sessoes_por_filme(
    filme_id: int,
    session: Session = Depends(obter_sessao)
):
    return listar_sessoes_por_filme(session, filme_id)