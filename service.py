from model import Task


class TaskService:
    def __init__(self, db):
        self.tasks = db.load_tasks()
        self.db = db

    def add_task(self, task):
        id = max(self.tasks) + 1 if self.tasks else 1
        new_task = Task(
            id=id,
            title=task.title,
            description=task.description,
        )
        self.tasks.append(new_task)
        self.db.save_tasks(self.tasks)
        return new_task

    def get_tasks(self):
        return self.tasks

    def get_task(self, id):
        return next((task for task in self.tasks if task.id == id), None)

    def delete_task(self, id):
        self.tasks = [task for task in self.tasks if task.id != id]
        self.db.save_tasks(self.tasks)

    def update_task(self, id, new_task):
        task = next((task for task in self.tasks if task.id == id), None)
        if task is not None:
            task.title = new_task.title
            task.description = new_task.description
            task.status = new_task.status
        self.db.save_tasks(self.tasks)
        return task

    def clear_tasks(self):
        self.tasks = []
        self.db.save_tasks(self.tasks)
