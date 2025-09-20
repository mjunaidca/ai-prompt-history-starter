import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_hello_endpoint():
    """Test that GET /hello returns 200 with correct JSON response."""
    response = client.get("/hello")
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


# RED PHASE: Failing tests that will drive implementation
def test_hello_endpoint_returns_correct_status_code():
    """Test that GET /hello returns exactly 200 status code."""
    response = client.get("/hello")
    assert response.status_code == 200


def test_hello_endpoint_returns_json_content_type():
    """Test that GET /hello returns JSON content type."""
    response = client.get("/hello")
    assert response.headers["content-type"] == "application/json"


def test_hello_endpoint_returns_expected_message():
    """Test that GET /hello returns the exact expected message."""
    response = client.get("/hello")
    data = response.json()
    assert data["message"] == "Hello World!"


def test_hello_endpoint_returns_only_required_fields():
    """Test that GET /hello returns only the required fields."""
    response = client.get("/hello")
    data = response.json()
    assert len(data) == 1
    assert "message" in data
    assert "timestamp" not in data  # This should fail initially
    assert "version" not in data    # This should fail initially


def test_hello_endpoint_handles_multiple_requests():
    """Test that GET /hello works consistently across multiple requests."""
    for i in range(3):
        response = client.get("/hello")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World!"}


def test_hello_endpoint_response_time():
    """Test that GET /hello responds within acceptable time."""
    import time
    start_time = time.time()
    response = client.get("/hello")
    end_time = time.time()
    
    assert response.status_code == 200
    assert (end_time - start_time) < 1.0  # Should respond within 1 second


def test_hello_endpoint_accepts_headers():
    """Test that GET /hello accepts various headers."""
    headers = {
        "Accept": "application/json",
        "User-Agent": "test-client"
    }
    response = client.get("/hello", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


# RED PHASE: These tests will FAIL - demonstrating what we need to implement
def test_hello_endpoint_returns_timestamp():
    """Test that GET /hello returns a timestamp field (WILL FAIL)."""
    response = client.get("/hello")
    data = response.json()
    assert "timestamp" in data  # This will fail - no timestamp in current implementation
    assert data["timestamp"] is not None


def test_hello_endpoint_returns_version():
    """Test that GET /hello returns a version field (WILL FAIL)."""
    response = client.get("/hello")
    data = response.json()
    assert "version" in data  # This will fail - no version in current implementation
    assert data["version"] == "0.1.0"


def test_hello_endpoint_handles_post_request():
    """Test that POST /hello works (WILL FAIL - only GET is implemented)."""
    response = client.post("/hello")
    assert response.status_code == 200  # This will fail - POST not implemented


def test_hello_endpoint_returns_detailed_response():
    """Test that GET /hello returns detailed response structure (WILL FAIL)."""
    response = client.get("/hello")
    data = response.json()
    expected_structure = {
        "message": "Hello World!",
        "status": "success",
        "timestamp": "2025-01-20T00:00:00Z",
        "version": "0.1.0"
    }
    assert data == expected_structure  # This will fail - current response is simpler


def test_hello_endpoint_handles_query_parameters():
    """Test that GET /hello?name=Test works (WILL FAIL)."""
    response = client.get("/hello?name=Test")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello Test!"  # This will fail - no query param handling


def test_hello_endpoint_returns_error_for_invalid_method():
    """Test that PUT /hello returns 405 Method Not Allowed (WILL FAIL)."""
    response = client.put("/hello")
    assert response.status_code == 405  # This will fail - FastAPI returns 405 by default
