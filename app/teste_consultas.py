from datetime import datetime
from app.database import engine, criar_tabelas
from app.models.filme import Filme
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
        # Preencha com os atributos existentes no seu modelo Sala.
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

    print(f"Filme cadastrado com ID: {filme.id}")
    print(f"Sala cadastrada com ID: {sala.id}")
    print(f"Sessão cadastrada com ID: {sessao.id}")

with Session(engine) as session:
    filmes = session.exec(select(Filme)).all()
    sessoes = session.exec(select(Sessao)).all()

    print("\n--- FILMES CADASTRADOS ---")

    for filme in filmes:
        print(f"ID: {filme.id} | Título: {filme.titulo}")

    print("\n--- SESSÕES CADASTRADAS ---")

    for sessao in sessoes:
        print(
            f"ID: {sessao.id} | "
            f"Filme ID: {sessao.filme_id} | "
            f"Sala ID: {sessao.sala_id}"
        )