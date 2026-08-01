"""
API routes for the Smart Expense Tracker.

This module defines all REST API endpoints related to expense management.
"""

from fastapi import APIRouter, HTTPException

from src.models import Expense, ExpenseCreate
from src.services import (
    add_expense,
    calculate_total,
    delete_expense,
    get_all_expenses,
    get_expenses_by_category,
)

router = APIRouter(
    tags=["Expenses"],
)


@router.post(
    "/expenses",
    response_model=Expense,
    status_code=201,
    summary="Create a new expense",
)
def create_expense(expense: ExpenseCreate) -> Expense:
    """
    Create a new expense.

    Args:
        expense: Expense information provided by the client.

    Returns:
        Expense: The newly created expense.
    """
    return add_expense(expense)


@router.get(
    "/expenses",
    summary="Retrieve expenses",
)
def read_expenses(category: str | None = None) -> list[dict]:
    """
    Retrieve all expenses or filter them by category.

    Args:
        category: Optional expense category.

    Returns:
        list[dict]: List of matching expenses.
    """
    if category:
        return get_expenses_by_category(category)

    return get_all_expenses()


@router.get(
    "/expenses/total",
    summary="Calculate total expenses",
)
def total_expenses(category: str | None = None) -> dict:
    """
    Calculate the total expense amount.

    Args:
        category: Optional expense category.

    Returns:
        dict: Total expense amount.
    """
    return calculate_total(category)


@router.delete(
    "/expenses/{expense_id}",
    summary="Delete an expense",
)
def remove_expense(expense_id: int) -> dict:
    """
    Delete an expense by its unique identifier.

    Args:
        expense_id: Expense identifier.

    Returns:
        dict: Success message.

    Raises:
        HTTPException: If the expense does not exist.
    """
    deleted = delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Expense not found.",
        )

    return {
        "message": "Expense deleted successfully."
    }