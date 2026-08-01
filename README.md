# Smart Expense Tracker API

## Overview

Smart Expense Tracker API is a RESTful web service built with **FastAPI** that allows users to manage personal expenses. It supports creating, retrieving, filtering, calculating totals, and deleting expenses. Expense data is stored in a local JSON file, so no database setup is required.

---

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Automatic request validation using Pydantic
- Interactive Swagger/OpenAPI documentation
- Unit tests using pytest

---

## Technology Stack

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn
- Pytest

---

## Project Structure

```
expense-tracker-api/
│
├── README.md
├── AI_NOTES.md
├── LICENSE
├── requirements.txt
├── pytest.ini
├── .gitignore
├── .editorconfig
│
├── data/
│   └── expenses.json
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│   └── storage.py
│
├── tests/
│   └── test_api.py
│
└── venv/
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Navigate to the project.

```bash
cd expense-tracker-api
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Server

Start the FastAPI development server.

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

OpenAPI schema:

```
http://127.0.0.1:8000/openapi.json
```

---

## Running the Tests

Run all automated tests.

```bash
pytest
```

Expected output:

```
6 passed
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/expenses` | Create a new expense |
| GET | `/expenses` | Retrieve all expenses |
| GET | `/expenses?category=Food` | Filter expenses by category |
| GET | `/expenses/total` | Calculate total expenses |
| GET | `/expenses/total?category=Food` | Calculate total by category |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## Sample Request

### Create Expense

```json
{
    "title": "Pizza",
    "amount": 350,
    "category": "Food",
    "date": "2026-08-02"
}
```

### Sample Response

```json
{
    "id": 1,
    "title": "Pizza",
    "amount": 350,
    "category": "Food",
    "date": "2026-08-02"
}
```

---

## Design Decisions

- FastAPI was selected for its simplicity, performance, and automatic OpenAPI documentation.
- Expense data is stored in a local JSON file as specified in the assignment.
- The application is divided into models, routes, services, and storage layers to maintain separation of concerns.
- Pydantic is used for request validation.
- Business logic is isolated from the API layer to improve maintainability and testability.

---

## Future Improvements

If the project were extended further, the following enhancements could be added:

- Database support (SQLite or PostgreSQL)
- User authentication and authorization
- Expense update endpoint
- Pagination and sorting
- Search functionality
- Docker support
- CI/CD pipeline

---

## License

This project is licensed under the MIT License.
