"""
Application entry point for the Smart Expense Tracker API.

This module creates the FastAPI application, registers all API routes,
and exposes the root endpoint.
"""

from fastapi import FastAPI

from src.routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="A REST API to manage personal expenses.",
    version="1.0.0",
)

app.include_router(router)


@app.get(
    "/",
    summary="Application Home",
)
def root() -> dict[str, str]:
    """
    Root endpoint of the application.

    Returns:
        dict[str, str]: Welcome message and API documentation URL.
    """

    return {
        "message": "Welcome to Smart Expense Tracker API!",
        "docs": "/docs",
    }