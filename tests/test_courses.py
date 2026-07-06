import uuid


def _unique_title():
    return f"Corso Test {uuid.uuid4().hex[:8]}"


def test_create_course(client):
    payload = {
        "title": _unique_title(),
        "category": "Python",
        "description": "Corso introduttivo",
        "active": True
    }
    response = client.post("/courses", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "Python"
    assert "_id" in data

    # cleanup
    client.delete(f"/courses/{data['_id']}")


def test_get_courses(client):
    response = client.get("/courses")
    assert response.status_code == 200
    data = response.json()
    assert "count" in data
    assert "data" in data


def test_get_course_by_id(client):
    payload = {
        "title": _unique_title(),
        "category": "DevOps",
        "description": "Corso avanzato",
        "active": True
    }
    created = client.post("/courses", json=payload).json()

    response = client.get(f"/courses/{created['_id']}")
    assert response.status_code == 200
    assert response.json()["category"] == "DevOps"

    # cleanup
    client.delete(f"/courses/{created['_id']}")


def test_get_course_by_id_not_found(client):
    response = client.get("/courses/000000000000000000000000")
    assert response.status_code == 404


def test_update_course(client):
    payload = {
        "title": _unique_title(),
        "category": "Database",
        "description": "Corso base",
        "active": True
    }
    created = client.post("/courses", json=payload).json()

    update_payload = {"active": False, "description": "Aggiornato"}
    response = client.put(f"/courses/{created['_id']}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["active"] is False
    assert data["description"] == "Aggiornato"

    # cleanup
    client.delete(f"/courses/{created['_id']}")


def test_delete_course(client):
    payload = {
        "title": _unique_title(),
        "category": "Cloud",
        "description": "Corso cloud",
        "active": True
    }
    created = client.post("/courses", json=payload).json()

    response = client.delete(f"/courses/{created['_id']}")
    assert response.status_code == 200

    check = client.get(f"/courses/{created['_id']}")
    assert check.status_code == 404


def test_delete_course_not_found(client):
    response = client.delete("/courses/000000000000000000000000")
    assert response.status_code == 404


def test_search_courses_by_category(client):
    category = f"CatTest{uuid.uuid4().hex[:6]}"
    payload = {
        "title": _unique_title(),
        "category": category,
        "description": "Corso ricerca",
        "active": True
    }
    created = client.post("/courses", json=payload).json()

    response = client.get(f"/courses/search/category/{category}")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] >= 1
    assert any(c["_id"] == created["_id"] for c in data["data"])

    # cleanup
    client.delete(f"/courses/{created['_id']}")