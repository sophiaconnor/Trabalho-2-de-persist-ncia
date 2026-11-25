from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import DateTime, Field, Session
from datetime import datetime
from datetime import date
from app.database import obter_ingresso
from app.services.ingressos_service import consultar_filmes_mais_populares, contar_ingressos_por_sessao
from app.database import obter_sessao
from app.services.ingressos_service import contar_ingressos_por_periodo

router = APIRouter(prefix="/ingressos", tags=["Ingressos"])

@router.get("/sessoes/{sessao_id}/quantidade")
def quantidade_ingressos_por_sessao_(
    sessao_id: int,
    cliente_nome: str | None = None,
    session: Session = Depends(obter_sessao)
):
    return contar_ingressos_por_sessao(
        session, sessao_id, cliente_nome
    )

@router.get("/periodo/quantidade")
def quantidade_ingressos_por_periodo(
    mes_inicio: int = Query(...),
    mes_fim: int = Query(...),
    ano: int = Query(..., ge=2000),
    session: Session = Depends(obter_sessao)
):
    if mes_inicio not in range(1, 13) or mes_fim not in range(1, 13):
        raise HTTPException(
            status_code=422,
            detail="Mês inválido. Escolha um mês entre 1 e 12."
        )
    return contar_ingressos_por_periodo(
        session, mes_inicio, mes_fim, ano
    )

@router.get("/filmes/mais-populares")
def filmes_mais_populares(
    limite: int = Query(...),
    session: Session = Depends(obter_sessao)
):
    return consultar_filmes_mais_populares(session, limite)