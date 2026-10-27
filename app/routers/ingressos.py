from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import obter_ingresso
from app.services.ingressos_service import listar_ingressos_por_cliente

router = APIRouter(prefix="/ingressos", tags=["Ingressos"])

@router.get("/cliente/{nome_cliente}")
def consultar_ingressos_por_cliente(
    nome_cliente: str,
    session: Session = Depends(obter_ingresso)
):
    return listar_ingressos_por_cliente(session, nome_cliente)