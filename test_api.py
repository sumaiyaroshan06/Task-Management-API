
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Learn API testing", "completed": False}
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn API testing"
    assert response.json()["completed"] is False


def test_missing_title():
    response = client.post(
        "/tasks",
        json={"completed": False}
    )

    assert response.status_code == 422


def test_get_all_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_nonexistent_task():
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_empty_title():
    response = client.post(
        "/tasks",
        json={"title": ""}
    )

    assert response.status_code == 422


def test_invalid_title_type():
    response = client.post(
        "/tasks",
        json={"title": 123}
    )

    assert response.status_code == 422


def test_get_created_task():
    create_response = client.post(
        "/tasks",
        json={"title": "Test task retrieval"}
    )

    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Test task retrieval"

