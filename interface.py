import json
import os
import sys

task_file = "tasks.json"


def load_tasks():
    tasks = []
    if os.path.exists(task_file):
        with open(task_file, "r") as file:
            tasks = json.load(file)
    return tasks


def save_tasks(tasks):
    with open(task_file, "w") as file:
        json.dump(tasks, file)


def menu():
    print("1. Dodaj zadanie")
    print("2. Lisa zadań")
    print("3. Zadanie")
    print("4. Usuń zadanie")
    print("5. Aktualizuj zadanie")
    print("0.  Wyjście")
    choice = input("Wybierz jedną z opcji: ")
    return choice


def add_task(tasks):
    title = input("Podaj tytuł: ")
    description = input("Podaj opis: ")
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "status": "do zrobienia",
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Zadanie dodane")


def list_tasks(tasks):
    for task in tasks:
        print(f"{task['id']}. {task['title']} - {task['status']}")


def get_task(tasks):
    id = int(input("Podaj id zadania: "))
    task = next((task for task in tasks if task["id"] == id), None)
    if task is None:
        print("Nie znaleziono zadania")
    else:
        print(f"{task['title']} - {task['description']} - {task['status']}")


def delete_task(tasks):
    id = int(input("Podaj id zadania: "))
    tasks = [task for task in tasks if task["id"] != id]
    save_tasks(tasks)
    print("Zadanie usunięte")


def update_task(tasks):
    id = int(input("Podaj id zadania: "))
    task = next((task for task in tasks if task["id"] == id), None)
    if task is None:
        print("Nie znaleziono zadania")
    else:
        title = input(f"Podaj nowy tytuł ({task['title']}): ")
        description = input(f"Podaj nowy opis ({task['description']}): ")
        status = input(f"Podaj nowy status ({task['status']}): ")
        task["title"] = title if title else task["title"]
        task["description"] = (
            description if description else task["description"]
        )
        task["status"] = status if status else task["status"]
        save_tasks(tasks)
        print("Zadanie zaktualizowane")


def main():
    tasks = load_tasks()
    while True:
        choice = menu()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            get_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            update_task(tasks)
        elif choice == "0":
            break
        else:
            print("Nieznana opcja")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Zamknięcie programu z klawiatury")
