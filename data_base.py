import json
import os


class DataBase:
    def __init__(self):
        self.task_file = "tasks.json"

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.task_file):
            with open(self.task_file, "r") as file:
                tasks = json.load(file)
        return tasks

    def save_tasks(self, tasks):
        tasks = [task.__dict__ for task in tasks]
        with open(self.task_file, "w") as file:
            json.dump(tasks, file)
