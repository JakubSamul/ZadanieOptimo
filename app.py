from flask import Flask, abort, jsonify, request

from data_base import DataBase
from model import Task
from service import TaskService

app = Flask(__name__)

db = DataBase()

service = TaskService(db)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = service.add_task(Task(**data))
    return jsonify(task.__dict__), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(service.get_tasks())


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = service.get_task(id)
    if task is None:
        abort(404, description="Nie znaleziono zadania")
    return jsonify(task)


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    service.delete_task(id)
    return "", 204


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = service.get_task(id)
    if task is None:
        abort(404, description="Nie znaleziono zadania")
    data = request.get_json()
    data["id"] = id
    task = service.update_task(id, Task(**request.get_json()))
    return jsonify(task)


if __name__ == "__main__":
    app.run(debug=True)
