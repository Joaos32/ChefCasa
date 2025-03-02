from fastapi import FastAPI
from app.routes import user, auth, chef  # Adicionando a rota de chefs

app = FastAPI(
    title="ChefCasa API",
    description="API para gerenciar usuários, chefs e autenticação no ChefCasa.",
    version="1.0.0"
)

# Registrar rotas
app.include_router(user.router, prefix="/users", tags=["Usuários"])
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(chef.router, prefix="/chefs", tags=["Chefs"])  # Adicionando a nova rota

# Rota raiz de teste
@app.get("/")
def read_root():
    return {"message": "API do ChefCasa está rodando!"}
