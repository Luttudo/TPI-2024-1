#  Crie uma API para cadastro de usuários, permitindo a inclusão, consulta, atualização e
# exclusão de usuários.
# Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados

from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI()

# Dados simulados (substitua pelo arquivo real)
users_data = {"users": []}

class User:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

@app.post("/usuarios/", response_model=User)
def cadastrar_usuario(user: User):
    # Verifica se o usuário já existe
    for existing_user in users_data["users"]:
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="Usuário já existe")
    
    # Valida a senha
    if len(user.senha) < 8:
        raise HTTPException(status_code=400, detail="Senha deve ter no mínimo 8 caracteres")
    
    # Adiciona o usuário aos dados simulados
    users_data["users"].append(user)
    return user

@app.get("/usuarios/", response_model=List[User])
def listar_usuarios():
    return users_data["users"]

# Implemente as rotas de atualização e exclusão de usuários
# ...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
