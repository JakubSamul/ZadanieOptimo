import json
import os

from flask import Flask, abort, jsonify, request

app = Flask(__name__)

tasks = []
task_file = "tasks.json"

if os.path.exists(task_file):
    with open(task_file, "r") as file:
        tasks = json.load(file)


class Task:
    def __init__(self, id, title, description, status="do zrobienia"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if data.get("title") or data.get("description") == "":
        abort(
            400,
            description="Tytuł i opis są wymagane i nie mogą być puste",
        )
    new_task = Task(
        id=len(tasks) + 1, title=data["title"], description=data["description"]
    )
    tasks.append(new_task.__dict__)
    save_tasks()
    return jsonify(new_task.__dict__), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    task = next((task for task in tasks if task["id"] == id), None)
    if task is None:
        abort(404, description="Nie znaleziono zadania")
    return jsonify(task)


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task["id"] != id]
    for index, task in enumerate(tasks):
        task["id"] = index + 1
    save_tasks()
    return "", 204


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = next((task for task in tasks if task["id"] == id), None)
    if task is None:
        abort(404, description="Nie znaleziono zadania")
    data = request.get_json()
    if "title" in data and not data["title"]:
        abort(400, description="Tytył nie może być pusty")
    if "description" in data and not data["description"]:
        abort(400, description="Opis nie może być pusty")
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["status"] = data.get("status", task["status"])
    save_tasks()
    return jsonify(task)


def save_tasks():
    with open(task_file, "w") as file:
        json.dump(tasks, file)


if __name__ == "__main__":
    app.run(debug=True)
