# To-Do API com FastAPI

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

API RESTful completa para gerenciamento de tarefas (To-Do List) com **CRUD completo**, validação de dados e documentação automática.

## 🚀 Funcionalidades
- Criar, listar, atualizar e deletar tarefas
- Marcar tarefas como concluídas
- Validação automática com Pydantic
- Documentação interativa (Swagger UI em `/docs`)

## 🛠 Tecnologias
- FastAPI
- SQLAlchemy 2.0
- Pydantic
- SQLite (fácil troca para PostgreSQL)

## 📦 Como rodar localmente
```bash
git clone https://github.com/SEU_USUARIO/todo-api-fastapi.git
cd todo-api-fastapi
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn[standard] sqlalchemy pydantic
python -m uvicorn app.main:app --reload