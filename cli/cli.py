"""
Command-line interface for the Todo App.

This module handles user input, command parsing, and output rendering.
"""

import re
from typing import Optional
from services.todo_service import TodoService


class CLI:
    """
    Command-line interface for the Todo App.
    """

    def __init__(self, todo_service: TodoService):
        """
        Initialize the CLI with a TodoService.

        Args:
            todo_service: The service to handle todo operations
        """
        self.todo_service = todo_service

    def run(self):
        """Run the main command loop."""
        while True:
            try:
                command_input = input("\ntodo> ").strip()

                if not command_input:
                    continue

                # Parse the command
                parts = command_input.split(maxsplit=1)
                command = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""

                # Handle the command
                if command == "quit" or command == "exit":
                    print("Goodbye!")
                    break
                elif command == "add":
                    self._handle_add(args)
                elif command == "view":
                    self._handle_view()
                elif command == "complete":
                    self._handle_complete(args)
                elif command == "delete":
                    self._handle_delete(args)
                elif command == "update":
                    self._handle_update(args)
                elif command == "help":
                    self._handle_help()
                else:
                    print(f"Error: Unknown command '{command}'. Use 'todo help' for available commands.")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def _handle_add(self, args: str):
        """Handle the add command."""
        title = self._extract_quoted_string(args)
        if not title:
            print("Error: Invalid command syntax. Use 'todo help' for usage information.")
            return

        if not self._is_valid_description(title):
            print("Error: Description must be 1-255 characters long.")
            return

        todo = self.todo_service.add_todo(title)
        if todo:
            print(f"Todo added with ID: {todo.id}")
        else:
            print("Error: Failed to add todo.")

    def _handle_view(self):
        """Handle the view command."""
        todos = self.todo_service.get_all_todos()

        if not todos:
            print("No todos found")
            return

        for todo in todos:
            status = "X" if todo.completed else "O"
            print(f"ID: {todo.id} | [{status}] | {todo.title}")

    def _handle_complete(self, args: str):
        """Handle the complete command."""
        todo_id = self._extract_id(args)
        if todo_id is None:
            print("Error: Invalid command syntax. Use 'todo help' for usage information.")
            return

        todo = self.todo_service.mark_complete(todo_id)
        if todo:
            print(f"Todo {todo_id} marked as complete")
        else:
            print(f"Error: Todo with ID {todo_id} does not exist.")

    def _handle_delete(self, args: str):
        """Handle the delete command."""
        todo_id = self._extract_id(args)
        if todo_id is None:
            print("Error: Invalid command syntax. Use 'todo help' for usage information.")
            return

        success = self.todo_service.delete_todo(todo_id)
        if success:
            print(f"Todo {todo_id} deleted successfully")
        else:
            print(f"Error: Todo with ID {todo_id} does not exist.")

    def _handle_update(self, args: str):
        """Handle the update command."""
        # Extract ID and new title from args like "1 'New title'"
        match = re.match(r'^(\d+)\s+(.+)$', args.strip(), re.DOTALL)
        if not match:
            print("Error: Invalid command syntax. Use 'todo help' for usage information.")
            return

        try:
            todo_id = int(match.group(1))
            title_part = match.group(2).strip()

            # Extract the new title from quotes
            new_title = self._extract_quoted_string(title_part)
            if not new_title:
                print("Error: Invalid command syntax. Use 'todo help' for usage information.")
                return

            if not self._is_valid_description(new_title):
                print("Error: Description must be 1-255 characters long.")
                return

            todo = self.todo_service.update_todo(todo_id, new_title)
            if todo:
                print(f"Todo {todo_id} updated successfully")
            else:
                print(f"Error: Todo with ID {todo_id} does not exist.")
        except ValueError:
            print("Error: Invalid command syntax. Use 'todo help' for usage information.")

    def _handle_help(self):
        """Handle the help command."""
        help_text = """
Available commands:
  add "description"     - Add a new todo with the given description
  view                 - View all todos with their status
  complete <id>        - Mark a todo as complete
  update <id> "desc"   - Update a todo's description
  delete <id>          - Delete a todo
  help                 - Show this help message
  quit/exit            - Exit the application

Examples:
  todo add "Buy groceries"
  todo view
  todo complete 1
  todo update 1 "Buy groceries - urgent"
  todo delete 1
        """.strip()
        print(help_text)

    def _extract_quoted_string(self, text: str) -> Optional[str]:
        """
        Extract a string wrapped in quotes from the input text.

        Args:
            text: The input text to extract from

        Returns:
            The extracted string if found, None otherwise
        """
        # Match both single and double quoted strings
        match = re.match(r'^["\'](.*)["\']$', text.strip())
        if match:
            return match.group(1)

        # Also match when the quoted string is at the beginning
        match = re.match(r'^["\'](.+?)["\']', text.strip())
        if match:
            return match.group(1)

        return None

    def _extract_id(self, text: str) -> Optional[int]:
        """
        Extract an integer ID from the input text.

        Args:
            text: The input text to extract from

        Returns:
            The extracted ID if found, None otherwise
        """
        text = text.strip()
        try:
            return int(text)
        except ValueError:
            # Try to extract ID from the beginning of the string
            match = re.match(r'^(\d+)', text)
            if match:
                return int(match.group(1))
            return None

    def _is_valid_description(self, description: str) -> bool:
        """
        Check if a description is valid (1-255 characters).

        Args:
            description: The description to validate

        Returns:
            True if valid, False otherwise
        """
        return 1 <= len(description) <= 255