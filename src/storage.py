"""
Storage layer for reading and writing expense data.

This module provides helper functions to load expenses from a JSON file,
save expenses back to the file, and generate unique expense IDs.
"""

import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "expenses.json"


def load_expenses() -> list[dict]:
    """
    Load all expenses from the JSON file.

    Returns:
        list[dict]: A list of expense dictionaries.
    """

    if not DATA_FILE.exists():
        DATA_DIR.mkdir(exist_ok=True)
        DATA_FILE.write_text("[]", encoding="utf-8")

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses: list[dict]) -> None:
    """
    Save expenses to the JSON file.

    Args:
        expenses: List of expense dictionaries.
    """

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def get_next_id(expenses: list[dict]) -> int:
    """
    Generate the next available expense ID.

    Args:
        expenses: List of existing expenses.

    Returns:
        int: The next available expense ID.
    """

    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1