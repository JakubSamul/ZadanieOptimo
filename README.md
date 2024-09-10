# 

Aplikacja webowa napisana w Pythonie z użyciem frameworka Flask. Aplikacja umożliwia zarządzanie zadaniami poprzez REST API.

## Wymagania

- Python 3.7+
- Flask
- Typing

## Instalacja

1. Sklonuj repozytorium:
    ```sh
    git clone https://github.com/JakubSamul/ZadanieOptimo.git
    cd ZadanieOptimo
    ```

2. Utwórz i aktywuj wirtualne środowisko:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Na Windows: venv\Scripts\activate
    ```

3. Zainstaluj wymagane pakiety:
    ```sh
    pip install -r requirements.txt
    ```

## Uruchomienie

1. Uruchom aplikację:
    ```sh
    flask run
    ```

2. Aplikacja będzie dostępna pod adresem `http://127.0.0.1:5000`.

## Endpointy

### Dodawanie zadania

- **URL:** `/tasks`
- **Metoda:** `POST`
- **Opis:** Dodaje nowe zadanie.
- **Body:** 
    ```json
    {
        "title": "Nazwa zadania",
        "description": "Opis zadania"
    }
    ```
- **Odpowiedź:** JSON zawierający dodane zadanie.
    ```json
    {
        "id": 1,
        "title": "Nazwa zadania",
        "description": "Opis zadania",
        "status": "do zrobienia"
    }
    ```

### Pobieranie wszystkich zadań

- **URL:** `/tasks`
- **Metoda:** `GET`
- **Opis:** Pobiera wszystkie zadania.
- **Odpowiedź:** 
    ```json
    [
        {
            "id": 1,
            "title": "Nazwa zadania",
            "description": "Opis zadania",
            "status": "do zrobienia"
        }
    ]
    ```

### Pobieranie zadania po ID

- **URL:** `/tasks/<int:id>`
- **Metoda:** `GET`
- **Opis:** Pobiera zadanie o podanym ID.
- **Odpowiedź:**
    ```json
    {
        "id": 1,
        "title": "Nazwa zadania",
        "description": "Opis zadania",
        "status": "do zrobienia"
    }
    ```

### Usuwanie zadania

- **URL:** `/tasks/<int:id>`
- **Metoda:** `DELETE`
- **Opis:** Usuwa zadanie o podanym ID.
- **Odpowiedź:** Brak treści, status 204.

### Aktualizacja zadania

- **URL:** `/tasks/<int:id>`
- **Metoda:** `PUT`
- **Opis:** Aktualizuje zadanie o podanym ID.
- **Body:** 
    ```json
    {
        "title": "Zaktualizowana nazwa zadania",
        "description": "Zaktualizowany opis zadania",
        "status": "w trakcie"
    }
    ```
- **Odpowiedź:** 
    ```json
    {
        "id": 1,
        "title": "Zaktualizowana nazwa zadania",
        "description": "Zaktualizowany opis zadania",
        "status": "w trakcie"
    }
    ```

### Aktualizacja statusu zadania

- **URL:** `/tasks/status/<int:id>`
- **Metoda:** `PUT`
- **Opis:** Aktualizuje status zadania o podanym ID.
- **Body:** 
    ```json
    {
        "status": "zakończone"
    }
    ```
- **Odpowiedź:** 
    ```json
    {
        "id": 1,
        "title": "Nazwa zadania",
        "description": "Opis zadania",
        "status": "zakończone"
    }
    ```

## Autor

Jakub Samul