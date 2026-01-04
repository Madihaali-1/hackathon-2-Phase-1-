"""
Todo data model representing a single task.

This module defines the Todo class with validation rules for title length,
ID positivity, and boolean status.
"""

from dataclasses import dataclass


@dataclass
class Todo:
    """
    Represents a single todo item.

    Attributes:
        id (int): Unique identifier for the todo (positive integer)
        title (str): Description of the task (1-255 characters)
        completed (bool): Completion status (default False)
    """

    id: int
    title: str
    completed: bool = False

    def __post_init__(self):
        """Validate the Todo attributes after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"ID must be a positive integer, got {self.id}")

        if not isinstance(self.title, str):
            raise ValueError(f"Title must be a string, got {type(self.title)}")

        if len(self.title) < 1 or len(self.title) > 255:
            raise ValueError(
                f"Title must be between 1 and 255 characters, got {len(self.title)} characters"
            )

        if not isinstance(self.completed, bool):
            raise ValueError(f"Completed must be a boolean, got {type(self.completed)}")