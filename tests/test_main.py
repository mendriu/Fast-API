def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_request_headers(client):
    response = client.get("/")
    assert "x-request-id" in response.headers
    assert "x-process-time" in response.headers
