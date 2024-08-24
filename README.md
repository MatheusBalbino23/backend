# Projeto de Gerenciamento de Filmes

Este é um projeto de API para gerenciamento de filmes utilizando FastAPI e SQLAlchemy. A API permite criar, listar e obter filmes a partir de um banco de dados SQLite.

## Funcionalidades

- **POST /Criar um filme**: Adiciona um novo filme ao banco de dados.
- **GET /Listar filmes**: Recupera todos os filmes armazenados no banco de dados.
- **GET /filmes/{id} /Obter um filme por ID**: Recupera um filme específico usando seu ID.

## Requisitos

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite (para banco de dados)
- Docker
- Git

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/MatheusBalbino23/backend.git
   cd backend
   ```

2. **Crie um ambiente virtual e ative-o:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuração do Banco de Dados

1. **Configure o banco de dados SQLite:**

   O banco de dados será criado automaticamente na primeira execução da aplicação.

## Executando a Aplicação

1. **Inicie o servidor FastAPI:**

   ```bash
   uvicorn app.main:app --reload
   ```

   O servidor estará disponível em `http://localhost:8000`.

## Uso com Docker

Para iniciar a aplicação utilizando Docker, siga os seguintes passos:

1. **Construa a imagem Docker** com o comando `docker-compose up --build`. Este comando irá criar a imagem Docker a partir do Dockerfile.
2. **Inicie os contêineres** com o comando `docker-compose up`. Este comando irá iniciar a aplicação e o banco de dados em contêineres separados.

## Testes

1. **Para rodar os testes:**

   ```bash
   pytest # Caso de erro use PYTHONPATH=. pytest
   ```

   Certifique-se de que o banco de dados de teste esteja limpo antes de rodar os testes.

## Endpoints

- **POST /filmes**: Adiciona um novo filme.

  - Corpo da requisição:
    ```json
    {
      "titulo": "Carros",
      "diretor": "John Lasseter",
      "ano": 2006
    }
    ```
  - Resposta:
    ```json
    {
      "id": 1,
      "titulo": "Carros",
      "diretor": "John Lasseter",
      "ano": 2006
    }
    ```

- **GET /filmes**: Lista todos os filmes.

  - Resposta:
    ```json
    [
      {
        "id": 1,
        "titulo": "Carros",
        "diretor": "John Lasseter",
        "ano": 2006
      }
    ]
    ```

- **GET /filmes/{id}**: Obtém um filme pelo ID.
  - Exemplo de requisição: `GET /filmes/1`
  - Resposta:
    ```json
    {
      "id": 1,
      "titulo": "Carros",
      "diretor": "John Lasseter",
      "ano": 2006
    }
    ```

## Problemas Conhecidos

- **Depreciações no Pydantic:** Algumas funcionalidades do Pydantic estão desatualizadas e podem gerar avisos. Estamos cientes dessas depreciações e planejamos atualizar o código conforme necessário.
