from fastapi.testclient import TestClient
from main import app  # Ajuste o caminho conforme necessário

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_auth():
    payload = {"username": "teste", "password": "senha123"}
    response = client.post("/login", json=payload)
    assert response.status_code in [200, 401]  # Pode falhar se as credenciais forem inválidas
