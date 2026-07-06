import uuid


def _unique_email():
    return f"test_{uuid.uuid4().hex[:8]}@example.com"


def test_create_user(client):
    payload = {
        "name": "Mario",
        "surname": "Rossi",
        "email": _unique_email(),
        "city": "Catania",
        "active": True
    }
    response = client.post("/users", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Mario"
    assert "_id" in data

    # cleanup
    client.delete(f"/users/{data['_id']}")


def test_create_user_duplicate_email(client):
    email = _unique_email()
    payload = {
        "name": "Luigi",
        "surname": "Verdi",
        "email": email,
        "city": "Roma",
        "active": True
    }
    first = client.post("/users", json=payload)
    assert first.status_code == 200
    user_id = first.json()["_id"]

    second = client.post("/users", json=payload)
    assert second.status_code == 400

    # cleanup
    client.delete(f"/users/{user_id}")


def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert "count" in data
    assert "data" in data


def test_get_user_by_id(client):
    payload = {
        "name": "Anna",
        "surname": "Bianchi",
        "email": _unique_email(),
        "city": "Milano",
        "active": True
    }
    created = client.post("/users", json=payload).json()

    response = client.get(f"/users/{created['_id']}")
    assert response.status_code == 200
    assert response.json()["email"] == payload["email"]

    # cleanup
    client.delete(f"/users/{created['_id']}")


def test_get_user_by_id_not_found(client):
    response = client.get("/users/000000000000000000000000")
    assert response.status_code == 404


def test_update_user(client):
    payload = {
        "name": "Paolo",
        "surname": "Neri",
        "email": _unique_email(),
        "city": "Torino",
        "active": True
    }
    created = client.post("/users", json=payload).json()

    update_payload = {"city": "Napoli", "active": False}
    response = client.put(f"/users/{created['_id']}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Napoli"
    assert data["active"] is False

    # cleanup
    client.delete(f"/users/{created['_id']}")


def test_delete_user(client):
    payload = {
        "name": "Giulia",
        "surname": "Russo",
        "email": _unique_email(),
        "city": "Bari",
        "active": True
    }
    created = client.post("/users", json=payload).json()

    response = client.delete(f"/users/{created['_id']}")
    assert response.status_code == 200

    # verify it's actually gone
    check = client.get(f"/users/{created['_id']}")
    assert check.status_code == 404


def test_delete_user_not_found(client):
    response = client.delete("/users/000000000000000000000000")
    assert response.status_code == 404


def test_search_users_by_city(client):
    city = f"CityTest{uuid.uuid4().hex[:6]}"
    payload = {
        "name": "Sara",
        "surname": "Conti",
        "email": _unique_email(),
        "city": city,
        "active": True
    }
    created = client.post("/users", json=payload).json()

    response = client.get(f"/users/search/city/{city}")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] >= 1
    assert any(u["_id"] == created["_id"] for u in data["data"])

    # cleanup
    client.delete(f"/users/{created['_id']}")
