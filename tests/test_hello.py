import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_hello_endpoint():
    """Test that GET /hello returns 200 with correct JSON response."""
    response = client.get("/hello")
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
