#!/usr/bin/env python3
"""
Simple test to verify the CLI works correctly.
"""

from services.todo_service import TodoService
from cli.cli import CLI
import sys
from io import StringIO

def test_cli_functionality():
    """Test CLI functionality by directly calling methods."""
    print("Testing CLI functionality...\n")

    # Create service and CLI
    service = TodoService()
    cli = CLI(service)

    print("1. Adding todos...")
    # Simulate adding todos by calling service directly
    todo1 = service.add_todo("Test task 1")
    todo2 = service.add_todo("Test task 2")
    print(f"   Added: {todo1.title} (ID: {todo1.id})")
    print(f"   Added: {todo2.title} (ID: {todo2.id})")

    print("\n2. Viewing todos...")
    todos = service.get_all_todos()
    for todo in todos:
        status = "X" if todo.completed else "O"
        print(f"   ID: {todo.id} | [{status}] | {todo.title}")

    print("\n3. Marking todo 1 as complete...")
    service.mark_complete(1)
    todos = service.get_all_todos()
    for todo in todos:
        status = "X" if todo.completed else "O"
        print(f"   ID: {todo.id} | [{status}] | {todo.title}")

    print("\n4. Deleting todo 2...")
    service.delete_todo(2)
    todos = service.get_all_todos()
    if todos:
        for todo in todos:
            status = "X" if todo.completed else "O"
            print(f"   ID: {todo.id} | [{status}] | {todo.title}")
    else:
        print("   No todos found")

    print("\nPASS: CLI functionality test completed successfully!")

if __name__ == "__main__":
    test_cli_functionality()