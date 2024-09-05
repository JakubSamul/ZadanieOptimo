from flask import Flask

app = Flask(__name__)


class Task:
    def __init__(self, id, title, description, status="do zrobienia"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status


if __name__ == "__main__":
    app.run(debug=True)
