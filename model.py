from dataclasses import dataclass
from dataclasses import field


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str = field(default="do zrobienia")
