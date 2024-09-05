from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_vowel_count():
    response = client.post("/vowel_count", json={"words": ["batman", "robin", "coringa"]})
    assert response.status_code == 200
    assert response.json() == {"batman": 2, "robin": 2, "coringa": 3}

def test_sort_asc():
    response = client.post("/sort", json={"words": ["batman", "robin", "coringa"], "order": "asc"})
    assert response.status_code == 200
    assert response.json() == ["batman", "coringa", "robin"]

def test_sort_desc():
    response = client.post("/sort", json={"words": ["batman", "robin", "coringa"], "order": "desc"})
    assert response.status_code == 200
    assert response.json() == ["robin", "coringa", "batman"]

def test_sort_invalid_order():
    response = client.post("/sort", json={"words": ["batman", "robin", "coringa"], "order": "invalid"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid order parameter"}
