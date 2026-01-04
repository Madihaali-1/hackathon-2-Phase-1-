#!/usr/bin/env python3
"""
Main entry point for the Todo App.

This console application allows users to manage their todo list in memory.
"""

from services.todo_service import TodoService
from cli.cli import CLI


def main():
    """Main application entry point."""
    print("Welcome to the Todo App!")
    print("\nAvailable commands:")
    print("  add \"description\"     - Add a new todo with the given description")
    print("  view                - View all todos with their status")
    print("  complete <id>       - Mark a todo as complete")
    print("  update <id> \"desc\"  - Update a todo's description")
    print("  delete <id>         - Delete a todo")
    print("  help                - Show this help message")
    print("  quit/exit           - Exit the application")
    print("\nExamples:")
    print("  add \"Buy groceries\"")
    print("  view")
    print("  complete 1")
    print("  update 1 \"Buy groceries - urgent\"")
    print("  delete 1")
    print()

    todo_service = TodoService()
    cli = CLI(todo_service)

    cli.run()


if __name__ == "__main__":
    main()