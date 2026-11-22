from sqlmodel import Field, Session, select
from app.models import sessao
from app.models.filme import Filme
from app.models.ingresso import Ingresso
from app.models.cliente import Cliente
from app.models.ingresso import Ingresso
from sqlalchemy import DateTime, func
from datetime import datetime
from datetime import date
from fastapi import Query
from app.models.sessao import Sessao
from sqlalchemy import extract

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

def contar_ingressos_por_periodo(
    session: Session,
    mes_inicio: int,
    mes_fim: int,
    ano: int
):
    consulta = (
        select(func.count(Ingresso.id))
        .join(Ingresso.sessao)
        .where(
            extract("month", Sessao.data_hora) >= mes_inicio,
            extract("month", Sessao.data_hora) <= mes_fim,
            extract("year", Sessao.data_hora) == ano
        )
    )

    return session.exec(consulta).one()

def consultar_filmes_mais_populares(session: Session, limite: int):
    consulta = select(
        Filme.titulo,
        func.count(Ingresso.id)
    ).join(Ingresso.sessao).join(Sessao.filme).group_by(Filme.titulo)

    resultado = session.exec(consulta).all()

    return [
        {
            "titulo": filme[0],
            "quantidade_ingressos": filme[1]
        }
        for filme in resultado
    ]