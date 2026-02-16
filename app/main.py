from fastapi import FastAPI
from app.routers import tasks
from app.database import engine
from app.models import Base  # Importa os modelos para registrar as tabelas

app = FastAPI(
    title="To-Do API",
    description="API RESTful para gerenciamento de tarefas com autenticação JWT",
    version="1.0.0"
)

# Cria as tabelas automaticamente ao iniciar a API
@app.on_event("startup")
def create_db():
    Base.metadata.create_all(bind=engine)
    print("Banco de dados verificado/criado com sucesso!")

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à To-Do API! Acesse /docs para a documentação."}