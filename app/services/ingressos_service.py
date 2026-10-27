from sqlmodel import Session, select
from app.models.ingresso import Ingresso
from app.models.cliente import Cliente

def listar_ingressos_por_cliente(session: Session, nome_cliente: str):
    consulta = (
        select(Ingresso)
        .join(Ingresso.cliente)
        .where(Cliente.nome == nome_cliente)
    )

    ingressos = session.exec(consulta).all()

    resultado = []

    for ingresso in ingressos:
        resultado.append({
            "ingresso_id": ingresso.id,
            "sessao_id": ingresso.sessao_id,
            "cliente_id": ingresso.cliente_id,
            "preco": ingresso.preco
        })

    return resultado