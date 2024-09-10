from database import DataBase
from models import Task, TaskCreateModel
from service import TaskService

db = DataBase()

service = TaskService(db)


def menu():
    while True:
        print("1. Dodaj zadanie")
        print("2. Lista zadań")
        print("3. Pokaż zadanie")
        print("4. Usuń zadanie")
        print("5. Aktualizuj zadanie")
        print("6. Aktualizuj status")
        print("0. Wyjście")
        choice = input("Wybierz jedną z opcji: \n")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            show_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            update_task()
        elif choice == "6":
            update_status()
        elif choice == "0":
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


def add_task():
    title = input("Podaj tytuł: ")
    description = input("Podaj opis: ")
    data = {"title": title, "description": description}
    task_data = TaskCreateModel(**data)
    task = service.add_task(task_data)
    print(
        f"Dodano zadanie: {task.id} - {task.title} - {task.description} - {task.status}"
    )


def list_tasks():
    for task in service.get_tasks():
        print(f"{task.id} - {task.title} - {task.description} - {task.status}")


def show_task():
    id = int(input("Podaj id zadania: "))
    task = service.get_task(id)
    if task is None:
        print("Nie znaleziono zadania")
    else:
        print(f"{task.id} - {task.title} - {task.description} - {task.status}")


def delete_task():
    id = int(input("Podaj id zadania: "))
    service.delete_task(id)
    print(f"Usunięto zadanie: {id}")


def update_task():
    id = int(input("Podaj id zadania: "))
    task = service.get_task(id)
    if task is None:
        print("Nie znaleziono zadania")
    else:
        title = input("Podaj nowy tytuł: ")
        description = input("Podaj nowy opis: ")
        status = input("Podaj nowy status: ")
        task = service.update_task(
            id, Task(id, title=title, description=description, status=status)
        )
        print(
            f"Zaktualizowano zadanie: {task.id} - {task.title} - {task.description} - {task.status}"
        )


def update_status():
    id = int(input("Podaj id zadania: "))
    task = service.get_task(id)
    if task is None:
        print("Nie znaleziono zadania")
    else:
        status = input("Podaj nowy status: ")
        task = service.update_status(id, status)
        print(
            f"Zaktualizowano status zadania: {task.id} - {task.title} - {task.description} - {task.status}"
        )


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("Zamknięcie programu z klawiatury")
