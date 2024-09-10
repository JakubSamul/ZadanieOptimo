from typing import Any, Dict, List, Tuple, Optional

from flask import Flask, Response, abort, jsonify, request

from database import DataBase
from models import Task, TaskCreateModel
from service import TaskService

app = Flask(__name__)

db = DataBase()

service = TaskService(db)


@app.route("/tasks", methods=["POST"])
def add_task() -> Tuple[Response, int]:
    data: Optional[Dict[str, Any]] = request.get_json()
    if data is None:
        abort(400, description="Nieprawidłowe dane wejściowe")
    task_data = TaskCreateModel(**data)
    task = service.add_task(task_data)
    return jsonify(task.__dict__), 201


@app.route("/tasks", methods=["GET"])
def get_tasks() -> Response:
    tasks: List[Task] = service.get_tasks()
    return jsonify([task.__dict__ for task in tasks])


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id: int) -> Response:
    task = service.get_task(id)
    if task is None:
        abort(404, description="Nie znaleziono zadania")
    return jsonify(task.__dict__)


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id: int) -> Tuple[str, int]:
    service.delete_task(id)
    return "", 204


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id: int) -> Response:
    task = service.get_task(id)
    if task is None:
        abort(404, description="Nie znaleziono zadania")
    data: Optional[Dict[str, Any]] = request.get_json()
    if data is None:
        abort(400, description="Nieprawidłowe dane wejściowe")
    data["id"] = id
    task = service.update_task(id, Task(**data))
    return jsonify(task.__dict__)


@app.route("/tasks/status/<int:id>", methods=["PUT"])
def update_status(id: int) -> Response:
    task = service.get_task(id)
    if task is None:
        abort(404, description="Nie znaleziono zadania")
    data: Optional[Dict[str, Any]] = request.get_json()
    if data is None or "status" not in data:
        abort(400, description="Nieprawidłowe dane wejściowe")
    task = service.update_status(id, data["status"])
    return jsonify(task.__dict__)


if __name__ == "__main__":
    app.run(debug=True)
