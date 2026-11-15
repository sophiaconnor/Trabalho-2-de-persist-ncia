from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import obter_ingresso
from app.services.ingressos_service import contar_ingressos_por_sessao
from app.database import obter_sessao

router = APIRouter(prefix="/ingressos", tags=["Ingressos"])

@router.get("/sessoes/{sessao_id}/quantidade")
def quantidade_ingressos(
    sessao_id: int,
    cliente_nome: str | None = None,
    session: Session = Depends(obter_sessao)
):
    return contar_ingressos_por_sessao(
        session, sessao_id, cliente_nome
    )