# Run as python -m pytest from project root
# to generate junit-style log use: python -m pytest --junitxml results.xml

from fastapi.testclient import TestClient

from api_impl.main import app

client = TestClient(app)

def test_read_home_nok():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}