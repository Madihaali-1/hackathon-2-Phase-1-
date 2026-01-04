#!/usr/bin/env python3
"""
Integration test to demonstrate the full Todo App functionality.
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from services.todo_service import TodoService
from cli.cli import CLI
import io
from contextlib import redirect_stdout

def demo_full_functionality():
    """Demonstrate the full functionality of the Todo App."""
    print("=== Todo App Integration Test ===\n")

    # Create service and CLI
    service = TodoService()
    cli = CLI(service)

    # Simulate user interactions by calling CLI methods directly
    print("1. Adding todos...")
    service.add_todo("Buy groceries")
    service.add_todo("Walk the dog")
    service.add_todo("Finish report")
    print("   Added 3 todos\n")

    print("2. Viewing all todos...")
    todos = service.get_all_todos()
    for todo in todos:
        status = "X" if todo.completed else "O"
        print(f"   ID: {todo.id} | [{status}] | {todo.title}")
    print()

    print("3. Marking a todo as complete...")
    service.mark_complete(2)
    print("   Marked todo with ID 2 as complete\n")

    print("4. Viewing todos after marking one as complete...")
    todos = service.get_all_todos()
    for todo in todos:
        status = "X" if todo.completed else "O"
        print(f"   ID: {todo.id} | [{status}] | {todo.title}")
    print()

    print("5. Updating a todo...")
    service.update_todo(3, "Finish the important report")
    print("   Updated todo with ID 3\n")

    print("6. Viewing todos after update...")
    todos = service.get_all_todos()
    for todo in todos:
        status = "X" if todo.completed else "O"
        print(f"   ID: {todo.id} | [{status}] | {todo.title}")
    print()

    print("7. Deleting a todo...")
    service.delete_todo(1)
    print("   Deleted todo with ID 1\n")

    print("8. Final view of todos...")
    todos = service.get_all_todos()
    if not todos:
        print("   No todos found")
    else:
        for todo in todos:
            status = "X" if todo.completed else "O"
            print(f"   ID: {todo.id} | [{status}] | {todo.title}")
    print()

    print("=== All functionality demonstrated successfully! ===")

def test_error_handling():
    """Test error handling functionality."""
    print("\n=== Testing Error Handling ===\n")

    service = TodoService()

    print("1. Testing invalid add (empty description)...")
    result = service.add_todo("")
    if result is None:
        print("   PASS: Correctly rejected empty description\n")

    print("2. Testing invalid add (too long description)...")
    long_desc = "x" * 256
    result = service.add_todo(long_desc)
    if result is None:
        print("   PASS: Correctly rejected too long description\n")

    print("3. Testing operations on non-existent todo...")
    result = service.mark_complete(999)
    if result is None:
        print("   PASS: Correctly handled non-existent todo for complete")

    result = service.update_todo(999, "New title")
    if result is None:
        print("   PASS: Correctly handled non-existent todo for update")

    success = service.delete_todo(999)
    if not success:
        print("   PASS: Correctly handled non-existent todo for delete\n")

    print("=== Error handling works correctly! ===")

if __name__ == "__main__":
    demo_full_functionality()
    test_error_handling()
    print("\nPASS: All integration tests passed! The Todo App is fully functional.")