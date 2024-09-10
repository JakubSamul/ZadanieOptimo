import json
import os
from typing import Any, Dict, List

from models import Task


class DataBase:
    def __init__(self) -> None:
        self.task_file = "tasks.json"

    def load_tasks(self) -> list[Task]:
        tasks = []
        if os.path.exists(self.task_file):
            with open(self.task_file, "r") as file:
                tasks = json.load(file)
                tasks = [Task(**task) for task in tasks]
        return tasks

    def save_tasks(self, tasks: List[Dict[str, Any]]) -> None:
        tasks = [task.__dict__ for task in tasks]
        with open(self.task_file, "w") as file:
            json.dump(tasks, file)
