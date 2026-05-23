from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_estudiantes_empty():
    response = client.get("/estudiantes")
    assert response.status_code == 200
    assert response.json() == []

def test_create_estudiante():
    payload = {
        "id": 1,
        "nombre": "Ana Torres",
        "correo": "ana@ut.edu.co",
        "programa": "Ing. Sistemas"
    }
    response = client.post("/estudiantes", json=payload)
    assert response.status_code == 201
    assert response.json()["nombre"] == "Ana Torres"