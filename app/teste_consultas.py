from datetime import datetime
from app.database import engine, criar_tabelas
from app.models import Ingresso
from app.models.cliente import Cliente
from app.models.filme import Filme
from app.models.genero import Genero
from app.models.ingresso import Ingresso
from app.models.sala import Sala
from app.models.sessao import Sessao
from sqlmodel import select, Session
from app.models.assento import Assento
from app.models.validacao import Validacao

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
        classificacao="14 anos"
    )
    session.add(filme)
    session.commit()
    session.refresh(filme)

    sala = Sala(
        numero=1,
        capacidade=100,
        tipo="2D"
    )

    session.add(sala)
    session.commit()
    session.refresh(sala)

    sessao1 = Sessao(
        data_hora=datetime(2026, 10, 27, 18, 0),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao1)
    session.commit()
    session.refresh(sessao1)

    sessao2 = Sessao(
        data_hora=datetime(2026, 10, 28, 18, 0),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao2)
    session.commit()
    session.refresh(sessao2)

    sessao3 = Sessao(
        data_hora=datetime(2026, 10, 29, 18, 0),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao3)
    session.commit()
    session.refresh(sessao3)

    sessao4 = Sessao(
        data_hora=datetime(2026, 10, 30, 18, 0),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao4)
    session.commit()
    session.refresh(sessao4)

    sessao5 = Sessao(
        data_hora=datetime(2026, 10, 31, 18, 0),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao5)
    session.commit()
    session.refresh(sessao5)

    sessao6 = Sessao(
        data_hora=datetime(2026, 11, 1, 18, 0),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao6)
    session.commit()
    session.refresh(sessao6)

    sessao7 = Sessao(
        data_hora=datetime(2026, 10, 27, 14, 20),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao7)
    session.commit()
    session.refresh(sessao7)

    sessao8 = Sessao(
        data_hora=datetime(2026, 10, 28, 14, 20),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao8)
    session.commit()
    session.refresh(sessao8)

    sessao9 = Sessao(
        data_hora=datetime(2026, 10, 29, 14, 20),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao9)
    session.commit()
    session.refresh(sessao9)

    sessao10 = Sessao(
        data_hora=datetime(2026, 10, 30, 14, 20),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao10)
    session.commit()
    session.refresh(sessao10)

    sessao11 = Sessao(
        data_hora=datetime(2026, 10, 31, 14, 20),
        preco=25.00,
        filme_id=filme.id,
        sala_id=sala.id
    )

    session.add(sessao11)
    session.commit()
    session.refresh(sessao11)

    genero = Genero(
        nome="Aventura",
        filmes=[filme]
    )

    session.add(genero)
    session.commit()
    session.refresh(genero)

    cliente = Cliente(
        nome="Sophia Muniz",
        email="sophia.muniz@06.com"
    )

    session.add(cliente)
    session.commit()
    session.refresh(cliente)

    assento = Assento(
    identificacao="A1",
    sala_id=sala.id
    )

    session.add(assento)
    session.commit()
    session.refresh(assento)

    ingresso = Ingresso(
    cliente_id=cliente.id,
    sessao_id=sessao1.id,
    preco=25.00,
    assento_id=assento.id
    )

    session.add(ingresso)
    session.commit()