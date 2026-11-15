from sqlmodel import Session, select

from app.models.assento import Assento
from app.models.sessao import Sessao
from app.models.ingresso import Ingresso


def listar_assentos_disponiveis(session: Session, sessao_id: int):

    # Buscar a sessão
    sessao = session.get(Sessao, sessao_id)

    if not sessao:
        return None

    # Buscar os assentos da sala
    consulta_assentos = select(Assento).where(
        Assento.sala_id == sessao.sala_id
    )

    assentos = session.exec(consulta_assentos).all()

    # Buscar os assentos que já possuem ingressos nessa sessão
    consulta_ocupados = select(Ingresso.assento_id).where(
        Ingresso.sessao_id == sessao_id
    )

    assentos_ocupados = set(session.exec(consulta_ocupados).all())

    # Verificar a disponibilidade
    resultado = []

    for assento in assentos:
        resultado.append({
            "assento_id": assento.id,
            "identificacao": assento.identificacao,
            "disponivel": assento.id not in assentos_ocupados
        })

    return resultado