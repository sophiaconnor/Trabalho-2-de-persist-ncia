from sqlmodel import Session, select
from datetime import timedelta
from app.models.filme import Filme
from app.models.sessao import Sessao
from app.models.sala import Sala
from app.routers import sessoes


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

def listar_sessoes_por_sala(session: Session, numero: int):
    consulta = (
        select(Sessao)
        .join(Sessao.sala)
        .where(Sala.numero == numero)
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


def verificar_conflito(
    session: Session,
    sala_id: int,
    data_hora,
    duracao_minutos: int
):
    inicio_atual = data_hora
    fim_atual = inicio_atual + timedelta(minutes=duracao_minutos)

    consulta = select(Sessao).where(
        Sessao.sala_id == sala_id
    )

    sessoes = session.exec(consulta).all()

    for sessao in sessoes:
        inicio_anterior = sessao.data_hora
        fim_anterior = inicio_anterior + timedelta(
            minutes=sessao.filme.duracao_minutos
        )

        if not (inicio_atual >= fim_anterior or fim_atual <= inicio_anterior):
            return True
    return False