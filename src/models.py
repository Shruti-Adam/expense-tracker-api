"""
Pydantic models for the Smart Expense Tracker API.
"""

import datetime

from pydantic import BaseModel, Field


class ExpenseBase(BaseModel):
    """
    Shared expense fields used across request and response models.
    """

    title: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Title of the expense",
    )

    amount: float = Field(
        ...,
        gt=0,
        description="Expense amount",
    )

    category: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Expense category",
    )

    date: datetime.date = Field(
        ...,
        description="Expense date",
    )


class ExpenseCreate(ExpenseBase):
    """
    Model used when creating a new expense.
    """

    pass


class Expense(ExpenseBase):
    """
    Model returned in API responses.
    """

    id: int = Field(
        ...,
        description="Unique expense identifier",
    )