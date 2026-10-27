from sqlmodel import Session, select

from app.models.filme import Filme
from app.models.sessao import Sessao


def listar_sessoes_por_filme(session: Session, titulo: str):
    consulta = (
        select(Sessao)
        .join(Sessao.filme)
        .where(Filme.titulo == titulo)
        .order_by(Sessao.data_hora)
    )

    sessoes = session.exec(consulta).all()

    resultado = []

    for sessao in sessoes:
        resultado.append({
            "filme": sessao.filme.titulo,
            "sessao_id": sessao.id,
            "data_hora": sessao.data_hora,
            "preco": sessao.preco,
            "sala_id": sessao.sala_id
        })

    return resultado
