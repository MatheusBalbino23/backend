import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base

# Cria uma instância do cliente de teste
client = TestClient(app)

# Configura e cria as tabelas no banco de dados para os testes
@pytest.fixture(scope="module")
def setup_database():
    # Cria as tabelas
    Base.metadata.create_all(bind=engine)
    
    # Define um teste de configuração do banco de dados
    yield
    
    # Não excluímos o banco de dados aqui; isso pode ser feito manualmente se necessário
    # Base.metadata.drop_all(bind=engine)  # Remova o banco de dados após os testes

@pytest.fixture
def db_session():
    # Cria uma nova sessão de banco de dados para cada teste
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

def test_create_and_read_filmes(db_session):
    # Adicionar filmes
    response = client.post("/filmes", json={
        "titulo": "Carros",
        "diretor": "John Lasseter",
        "ano": 2006
    })
    assert response.status_code == 200
    created_filme = response.json()
    assert created_filme["titulo"] == "Carros"
    assert created_filme["diretor"] == "John Lasseter"
    assert created_filme["ano"] == 2006

    response = client.post("/filmes", json={
        "titulo": "Carros 2",
        "diretor": "John Lasseter, Brad Lewis",
        "ano": 2011
    })
    assert response.status_code == 200
    created_filme = response.json()
    assert created_filme["titulo"] == "Carros 2"
    assert created_filme["diretor"] == "John Lasseter, Brad Lewis"
    assert created_filme["ano"] == 2011

    response = client.post("/filmes", json={
        "titulo": "Carros 3",
        "diretor": "Brian Fee",
        "ano": 2017
    })
    assert response.status_code == 200
    created_filme = response.json()
    assert created_filme["titulo"] == "Carros 3"
    assert created_filme["diretor"] == "Brian Fee"
    assert created_filme["ano"] == 2017

    # Verificar todos os filmes
    response = client.get("/filmes")
    assert response.status_code == 200
    filmes = response.json()
    assert len(filmes) == 3
