from sqlmodel import Session, select
from app.models.ingresso import Ingresso
from app.models.cliente import Cliente
from app.models.ingresso import Ingresso
from sqlalchemy import func

def cancelar_ingresso(session: Session, ingresso_id: int):
    ingresso = session.get(Ingresso, ingresso_id)

    if not ingresso:
        return False

    session.delete(ingresso)
    session.commit()

    return True

def contar_ingressos_por_sessao(
    session: Session,
    sessao_id: int,
    cliente_nome: str | None = None
):
    consulta = select(func.count(Ingresso.id)).where(
        Ingresso.sessao_id == sessao_id
    )

    if cliente_nome is not None:
        consulta = consulta.where(
            Ingresso.cliente.has(Cliente.nome == cliente_nome)
        )

    return session.exec(consulta).one()