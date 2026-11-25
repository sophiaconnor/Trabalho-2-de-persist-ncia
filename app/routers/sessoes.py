from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database import obter_sessao
from app.services.sessao_service import listar_sessoes_por_filme, listar_sessoes_por_sala

router = APIRouter(prefix="/sessoes", tags=["Sessões"])


@router.get("/filme/{titulo}")
def consultar_sessoes_por_filme(
    titulo: str,
    session: Session = Depends(obter_sessao),
    turno: str | None = None
):
    if turno is not None and turno not in ["tarde", "noite"]:
        raise HTTPException(
            status_code=422,
            detail="Turno inválido. Escolha tarde ou noite."
        )
    return listar_sessoes_por_filme(session, titulo, turno)

@router.get("/sala/{numero}")
def consultar_sessoes_por_sala(
    numero: int,
    page: int,
    page_size: int = 10,
    session: Session = Depends(obter_sessao),
    mês: int | None = None
):
    if mês is not None and mês not in range(1, 13):
        raise HTTPException(
            status_code=422,
            detail="Mês inválido. Escolha um mês entre 1 e 12."
        )
    return listar_sessoes_por_sala(session, numero, mês, page, page_size)