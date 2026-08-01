"""
Business logic for the Smart Expense Tracker API.

This module contains all business operations related to expenses.
It acts as an intermediary between the API routes and the storage layer.
"""

from src.models import Expense, ExpenseCreate
from src.storage import get_next_id, load_expenses, save_expenses


def add_expense(expense: ExpenseCreate) -> Expense:
    """
    Create and store a new expense.

    Args:
        expense: Expense details provided by the user.

    Returns:
        Expense: The newly created expense with an assigned ID.
    """

    expenses = load_expenses()

    expense_data = expense.model_dump()

    new_expense = Expense(
        id=get_next_id(expenses),
        **expense_data,
    )

    expenses.append(new_expense.model_dump(mode="json"))

    save_expenses(expenses)

    return new_expense


def get_all_expenses() -> list[dict]:
    """
    Retrieve all expenses.

    Returns:
        list[dict]: List of all stored expenses.
    """

    return load_expenses()


def get_expenses_by_category(category: str) -> list[dict]:
    """
    Retrieve expenses for a specific category.

    Args:
        category: Expense category.

    Returns:
        list[dict]: Matching expenses.
    """

    expenses = load_expenses()

    return [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]


def calculate_total(category: str | None = None) -> dict:
    """
    Calculate the total expense amount.

    Args:
        category: Optional expense category.

    Returns:
        dict: Total amount with optional category information.
    """

    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    total = sum(expense["amount"] for expense in expenses)

    return {
        "category": category,
        "total": total,
    }


def delete_expense(expense_id: int) -> bool:
    """
    Delete an expense by its ID.

    Args:
        expense_id: Expense identifier.

    Returns:
        bool:
            True if the expense was deleted.
            False if no matching expense was found.
    """

    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        return False

    save_expenses(updated_expenses)

    return True