from dataclasses import dataclass, field


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str = field(default="do zrobienia")


@dataclass
class TaskCreateModel:
    title: str
    description: str
