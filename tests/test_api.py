"""
Test suite for the Smart Expense Tracker API.
"""

import json
from pathlib import Path

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

DATA_FILE = Path("data/expenses.json")


def setup_function():
    """
    Reset the JSON data file before each test.
    """
    DATA_FILE.write_text("[]", encoding="utf-8")


def test_create_expense():
    """
    Test creating a new expense.
    """

    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 350,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Pizza"
    assert data["amount"] == 350
    assert data["category"] == "Food"


def test_get_all_expenses():
    """
    Test retrieving all expenses.
    """

    client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 120,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_by_category():
    """
    Test filtering expenses by category.
    """

    client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 120,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Bus",
            "amount": 50,
            "category": "Travel",
            "date": "2026-08-02",
        },
    )

    response = client.get(
        "/expenses",
        params={"category": "Food"},
    )

    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["category"] == "Food"


def test_calculate_total():
    """
    Test calculating the total expense amount.
    """

    client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 100,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 200,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 300


def test_delete_expense():
    """
    Test deleting an expense.
    """

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 350,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    response = client.delete("/expenses/1")

    assert response.status_code == 200

    response = client.get("/expenses")

    assert response.json() == []


def test_delete_non_existing_expense():
    """
    Test deleting a non-existing expense.
    """

    response = client.delete("/expenses/999")

    assert response.status_code == 404