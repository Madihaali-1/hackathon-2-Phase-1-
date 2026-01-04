"""
Todo repository for in-memory storage.

This module provides methods to store, retrieve, update, and delete
todo items in memory.
"""

from typing import List, Optional
from models.todo import Todo


class TodoRepository:
    """
    Repository for managing Todo items in memory.
    """

    def __init__(self):
        """Initialize the repository with an empty list of todos."""
        self._todos: List[Todo] = []
        self._next_id = 1

    def add(self, title: str) -> Todo:
        """
        Add a new todo with the given title.

        Args:
            title: The title of the new todo

        Returns:
            The newly created Todo object with an assigned ID
        """
        todo = Todo(id=self._next_id, title=title, completed=False)
        self._todos.append(todo)
        self._next_id += 1
        return todo

    def get_all(self) -> List[Todo]:
        """
        Retrieve all todos.

        Returns:
            A list of all Todo objects
        """
        return self._todos.copy()

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Retrieve a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The Todo object if found, None otherwise
        """
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def update(self, todo_id: int, title: str = None, completed: bool = None) -> Optional[Todo]:
        """
        Update a todo's attributes.

        Args:
            todo_id: The ID of the todo to update
            title: New title (optional)
            completed: New completion status (optional)

        Returns:
            The updated Todo object if found, None otherwise
        """
        todo = self.get_by_id(todo_id)
        if todo is None:
            return None

        if title is not None:
            todo.title = title
        if completed is not None:
            todo.completed = completed

        return todo

    def delete(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was found and deleted, False otherwise
        """
        todo = self.get_by_id(todo_id)
        if todo is None:
            return False

        self._todos.remove(todo)
        return True