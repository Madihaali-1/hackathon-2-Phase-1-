"""
Utility functions for validation.

This module provides validation functions for various input types.
"""


def validate_description(description: str) -> bool:
    """
    Validate a todo description.

    Args:
        description: The description to validate

    Returns:
        True if the description is valid, False otherwise
    """
    if not isinstance(description, str):
        return False

    if len(description) < 1 or len(description) > 255:
        return False

    return True


def validate_todo_id(todo_id: int) -> bool:
    """
    Validate a todo ID.

    Args:
        todo_id: The ID to validate

    Returns:
        True if the ID is valid, False otherwise
    """
    if not isinstance(todo_id, int):
        return False

    if todo_id <= 0:
        return False

    return True