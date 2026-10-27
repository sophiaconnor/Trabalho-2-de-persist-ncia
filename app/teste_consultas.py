from datetime import datetime
from app.database import engine, criar_tabelas
from app.models.cliente import Cliente
from app.models import cliente
from app.models.filme import Filme
from app.models.ingresso import Ingresso
from app.models.sala import Sala
from app.models.sessao import Sessao
from app.services.sessao_service import listar_sessoes_por_filme
from sqlmodel import select, Session

criar_tabelas()

with Session(engine) as session:
    filme = Filme(
        titulo="Wildwood: O bosque selvagem",
        sinopse=
        "Uma adolescente inicia uma missão" \
        " desesperada de resgate em uma floresta" \
        " encantada depois que seu irmãozinho é" \
        " raptado por um bando de corvos. Acompanhada" \
        " por um colega de classe azarado, ela arrisca" \
        " tudo ao navegar por um mundo cheio de bandidos," \
        " animais falantes e figuras poderosas.",
        duracao_minutos=130,
        gênero="Fantasia",
        classificacao="14 anos"
    )

    sala = Sala(
        numero=1,
        capacidade=100,
        tipo="2D"
    )

    session.add(filme)
    session.add(sala)
    session.commit()

    session.refresh(filme)
    session.refresh(sala)

    sessao = Sessao(
        data_hora=datetime(2026, 10, 27, 18, 0),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao)
    session.commit()
    session.refresh(sessao)
    

    cliente = Cliente(
        nome="Sophia Muniz",
        email="sophia.muniz@06.com"
    )

    session.add(cliente)
    session.commit()
    session.refresh(cliente)

    ingresso = Ingresso(
    cliente_id=cliente.id,
    sessao_id=sessao.id,
    preco=25.00
    )

    session.add(ingresso)
    session.commit()
    session.refresh(ingresso)