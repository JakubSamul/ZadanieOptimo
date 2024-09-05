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
            description="Title and description are required and cannot be empty",
        )
    new_task = Task(
        id=len(tasks) + 1, title=data["title"], description=data["description"]
    )
    tasks.append(new_task.__dict__)
    save_tasks()
    return jsonify(new_task.__dict__), 201


def save_tasks():
    with open(task_file, "w") as file:
        json.dump(tasks, file)


if __name__ == "__main__":
    app.run(debug=True)
