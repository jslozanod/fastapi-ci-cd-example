from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}


def test_say_hello():
    response = client.get("/hello/Juan")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Juan!"}

