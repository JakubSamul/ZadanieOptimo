from models import Task, TaskCreateModel
from typing import Optional


class TaskService:
    def __init__(self, db) -> None:
        self.tasks = db.load_tasks()
        self.db = db

    def add_task(self, task: TaskCreateModel) -> Task:
        ids = [task.id for task in self.tasks]
        id = max(ids) + 1 if ids else 1
        new_task = Task(
            id=id,
            title=task.title,
            description=task.description,
        )
        self.tasks.append(new_task)
        self.db.save_tasks(self.tasks)
        return new_task

    def get_tasks(self) -> list[Task]:
        return self.tasks

    def get_task(self, id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def delete_task(self, id: int) -> None:
        self.tasks = [task for task in self.tasks if task.id != id]
        self.db.save_tasks(self.tasks)

    def update_task(self, id: int, new_task: Task) -> Task:
        task = next((task for task in self.tasks if task.id == id), None)
        if task is not None:
            task.title = new_task.title
            task.description = new_task.description
            task.status = new_task.status
        self.db.save_tasks(self.tasks)
        return task

    def update_status(self, id: int, status: str) -> Task:
        task = next((task for task in self.tasks if task.id == id), None)
        if task is not None:
            task.status = status
        self.db.save_tasks(self.tasks)
        return task

    def clear_tasks(self):
        self.tasks = []
        self.db.save_tasks(self.tasks)
