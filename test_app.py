import json
import os
import shutil

import pytest

from app import app, service

task_file = "tasks.json"


@pytest.fixture
def client():
    app.testing = True
    user = app.test_client()
    if os.path.exists(task_file):
        shutil.copy(task_file, f"{task_file}.bak")
    service.clear_tasks()
    if os.path.exists(task_file):
        os.remove(task_file)
    yield user
    if os.path.exists(f"{task_file}.bak"):
        shutil.move(f"{task_file}.bak", task_file)


def test_add_task(client):
    response = client.post(
        "/tasks",
        data=json.dumps(
            {
                "title": "test",
                "description": "test",
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.json == {
        "id": 1,
        "title": "test",
        "description": "test",
        "status": "do zrobienia",
    }


def test_get_tasks(client):
    client.post(
        "/tasks",
        data=json.dumps(
            {
                "title": "test",
                "description": "test",
            }
        ),
        content_type="application/json",
    )
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == [
        {
            "id": 1,
            "title": "test",
            "description": "test",
            "status": "do zrobienia",
        }
    ]


def test_get_task(client):
    client.post(
        "/tasks",
        data=json.dumps(
            {
                "title": "test",
                "description": "test",
            }
        ),
        content_type="application/json",
    )
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "title": "test",
        "description": "test",
        "status": "do zrobienia",
    }


def test_update_task(client):
    client.post(
        "/tasks",
        data=json.dumps(
            {
                "title": "test",
                "description": "test",
            }
        ),
        content_type="application/json",
    )
    response = client.put(
        "/tasks/1",
        data=json.dumps(
            {
                "title": "test2",
                "description": "test2",
                "status": "w trakcie",
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "title": "test2",
        "description": "test2",
        "status": "w trakcie",
    }


def test_update_status(client):
    client.post(
        "/tasks",
        data=json.dumps(
            {
                "title": "test",
                "description": "test",
            }
        ),
        content_type="application/json",
    )
    response = client.put(
        "/tasks/status/1",
        data=json.dumps(
            {
                "title": "test",
                "description": "test",
                "status": "w trakcie",
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "title": "test",
        "description": "test",
        "status": "w trakcie",
    }


def test_delete_task(client):
    client.post(
        "/tasks",
        data=json.dumps(
            {
                "title": "test",
                "description": "test",
            }
        ),
        content_type="application/json",
    )
    response = client.delete("/tasks/1")
    assert response.status_code == 204
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == []
