def test_create_item(client):
    response = client.post(
        "/items/",
        json={"name": "Test Item", "price": 10.5, "description": "A test item"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["price"] == 10.5
    assert data["id"] == 1


def test_create_item_invalid_price(client):
    response = client.post(
        "/items/",
        json={"name": "Test Item", "price": -5}
    )
    assert response.status_code == 422


def test_list_items(client):
    client.post("/items/", json={"name": "Item 1", "price": 10.0})
    client.post("/items/", json={"name": "Item 2", "price": 20.0})

    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_get_item(client):
    client.post("/items/", json={"name": "Get Test", "price": 15.0})

    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Get Test"


def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404


def test_update_item(client):
    client.post("/items/", json={"name": "Original", "price": 10.0})

    response = client.put(
        "/items/1",
        json={"name": "Updated", "price": 25.0}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated"
    assert response.json()["price"] == 25.0


def test_update_item_not_found(client):
    response = client.put(
        "/items/999",
        json={"name": "Updated", "price": 25.0}
    )
    assert response.status_code == 404


def test_delete_item(client):
    client.post("/items/", json={"name": "To Delete", "price": 10.0})

    response = client.delete("/items/1")
    assert response.status_code == 204

    response = client.get("/items/1")
    assert response.status_code == 404


def test_delete_item_not_found(client):
    response = client.delete("/items/999")
    assert response.status_code == 404
