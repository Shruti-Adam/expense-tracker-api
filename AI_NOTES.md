# AI_NOTES.md

# AI Usage Summary

AI tools were used as a development assistant throughout this assignment to accelerate implementation, improve code quality, and review the overall project structure. All generated code was reviewed, validated, tested, and refined before being included in the final submission.

---

# AI Tools Used

- ChatGPT (GPT-5.5)

---

# AI-Assisted Components

AI assistance was used for the following tasks:

- Designing the overall project architecture.
- Creating the initial FastAPI application structure.
- Implementing Pydantic models for request and response validation.
- Implementing the JSON-based storage layer.
- Developing business logic for expense management.
- Implementing REST API endpoints.
- Writing automated tests using pytest.
- Preparing the README documentation.
- Reviewing the code for readability, maintainability, and Python best practices.

---

# Manual Validation and Changes

The AI-generated code was not used without review. The following validation and modifications were performed manually:

- Verified every source file for syntax errors using:

```bash
python -m py_compile
```

- Started the application locally using:

```bash
uvicorn src.main:app --reload
```

- Verified all REST API endpoints through the Swagger UI.

- Tested the following operations manually:

  - Create Expense
  - View All Expenses
  - Filter Expenses by Category
  - Calculate Total Expenses
  - Delete Expense

- Wrote and executed automated tests using pytest.

- Reviewed the project structure and refactored the code into separate modules (`models`, `routes`, `services`, and `storage`) to improve maintainability.

- Added type hints, module-level documentation, and improved function docstrings.

---

# Issues Encountered

During development, a compatibility issue occurred between Python 3.13 and Pydantic when using:

```python
from datetime import date
```

The issue was resolved by changing the implementation to:

```python
import datetime
```

and updating the model field to:

```python
date: datetime.date
```

The application was retested after applying this fix.

---

# AI Suggestions That Were Not Used

Some AI suggestions were intentionally not included:

- Database integration (SQLite/PostgreSQL), because the assignment explicitly requested JSON or in-memory storage.
- Additional CRUD operations such as updating an expense, because they were outside the assignment requirements.
- Authentication and authorization, because they were not part of the requested functionality.

---

# Final Verification

Before submission, the following checks were completed:

- Project structure reviewed.
- Source code reviewed for readability.
- PEP 8 formatting applied.
- FastAPI application started successfully.
- Swagger documentation verified.
- All automated tests passed successfully.

```
pytest
```

Result:

```
6 passed
```

---

# Contribution

AI was used as a development assistant for implementation guidance, code review, and documentation. The final project structure, testing, validation, debugging, and verification were completed through manual review and execution before submission.
