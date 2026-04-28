# FinnControl (Em desenvolvimento):
API REST para controle financeiro pessoal, desenvolvida com Python utilizando FastAPI e SQLAlchemy.

O projeto tem como objetivo simular um sistema real de backend, permitindo o gerenciamento de transações financeiras com categorização.

---

## Funcionalidades(por enquanto)
* CRUD completo de transações
  * Criar transações (POST)
  * Listar transações (GET)
  * Atualizar transações (PUT)
  * Deletar transações (DELETE)

* Sistema de categorias
  * Categorias padrão (Alimentação, Transporte, Lazer)
  * Criação de novas categorias
  * Relacionamento entre transações e categorias

  * Banco de dados relacional
  * Uso de SQLAlchemy (ORM)
  * Relacionamento entre tabelas (Foreign Key)

---

## Tecnologias utilizadas:
* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

---

## Conceitos aplicados
* Arquitetura de API REST
* ORM (Object Relational Mapping)
* Injeção de dependência
* Validação de dados
* Relacionamento entre entidades (1:N)

---

## Estrutura do projeto
app/main.py        # Rotas da API
app/models.py      # Modelos do banco (SQLAlchemy)
app/schemas.py     # Validação de dados (Pydantic)
app/database.py    # Configuração do banco

---

## Como rodar o projeto
1. Clone o repositório:

git clone https://github.com/RafaelMotta72/finncontrol.git
cd finncontrol

2. Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate

4. Instale as dependências:
pip install fastapi uvicorn sqlalchemy

4. Execute a aplicação:
uvicorn app.main:app --reload

5. Acesse a documentação automática:
http://127.0.0.1:8000/docs

---

##  Status do projeto:
Em desenvolvimento...

Próximas melhorias planejadas:

* Cálculo de saldo automático
* Filtro de transações por categoria
* Melhor organização das respostas da API
* Implementação de frontend

---

## Objetivo

Este projeto foi desenvolvido como prática de backend com foco em:

* construção de APIs reais
* integração com banco de dados
* aplicação de boas práticas de desenvolvimento

---

## Autor
Rafael Motta
Estudante de Engenharia de Software
