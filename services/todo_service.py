"""
Todo service for business logic.

This module provides methods to handle todo-related operations
with validation and error handling.
"""

from typing import List, Optional
from models.todo import Todo
from repositories.todo_repository import TodoRepository
from utils.validators import validate_description, validate_todo_id


class TodoService:
    """
    Service class for handling todo business logic.
    """

    def __init__(self):
        """Initialize the service with a repository."""
        self.repository = TodoRepository()

    def add_todo(self, title: str) -> Optional[Todo]:
        """
        Add a new todo with the given title.

        Args:
            title: The title of the new todo

        Returns:
            The newly created Todo object if successful, None otherwise
        """
        if not validate_description(title):
            return None

        return self.repository.add(title)

    def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all todos.

        Returns:
            A list of all Todo objects
        """
        return self.repository.get_all()

    def mark_complete(self, todo_id: int) -> Optional[Todo]:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            The updated Todo object if found, None otherwise
        """
        if not validate_todo_id(todo_id):
            return None

        return self.repository.update(todo_id, completed=True)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was found and deleted, False otherwise
        """
        if not validate_todo_id(todo_id):
            return False

        return self.repository.delete(todo_id)

    def update_todo(self, todo_id: int, new_title: str) -> Optional[Todo]:
        """
        Update a todo's title.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo

        Returns:
            The updated Todo object if found, None otherwise
        """
        if not validate_todo_id(todo_id) or not validate_description(new_title):
            return None

        return self.repository.update(todo_id, title=new_title)