"""
Tests
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_vowel_count():
    """Verify vowel counts for given words at /vowel_count."""
    response = client.post("/vowel_count", json={"words": ["batman", "robin", "coringa"]})
    assert response.status_code == 200
    assert response.json() == {"batman": 2, "robin": 2, "coringa": 3}

def test_sort_asc():
    """Check sorting in ascending order at /sort."""
    response = client.post("/sort", json={"words": ["batman", "robin", "coringa"], "order": "asc"})
    assert response.status_code == 200
    assert response.json() == ["batman", "coringa", "robin"]

def test_sort_desc():
    """Check sorting in descending order at /sort."""
    response = client.post("/sort", json={"words": ["batman", "robin", "coringa"], "order": "desc"})
    assert response.status_code == 200
    assert response.json() == ["robin", "coringa", "batman"]

def test_sort_invalid_order():
    """Verify error handling for invalid order at /sort."""
    response = client.post("/sort", json={"words": ["batman", "robin"], "order": "invalid"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid order parameter"}
