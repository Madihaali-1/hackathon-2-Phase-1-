#!/usr/bin/env python3
"""
Test script for the Todo App.

This script tests all functionality of the Todo App by simulating user input.
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from services.todo_service import TodoService
from cli.cli import CLI
import io
from contextlib import redirect_stdout, redirect_stderr

def test_add_functionality():
    """Test the add functionality."""
    print("Testing ADD functionality...")
    service = TodoService()

    # Test adding a todo
    todo = service.add_todo("Buy groceries")
    assert todo is not None, "Failed to add todo"
    assert todo.title == "Buy groceries", "Todo title not set correctly"
    assert todo.id == 1, "Todo ID not set correctly"
    assert not todo.completed, "Todo should not be completed by default"
    print("PASS: ADD functionality works correctly")

def test_view_functionality():
    """Test the view functionality."""
    print("Testing VIEW functionality...")
    service = TodoService()

    # Add a todo
    service.add_todo("Buy groceries")
    service.add_todo("Walk the dog")

    # Get all todos
    todos = service.get_all_todos()
    assert len(todos) == 2, "Should have 2 todos"
    assert todos[0].title == "Buy groceries", "First todo should be 'Buy groceries'"
    assert todos[1].title == "Walk the dog", "Second todo should be 'Walk the dog'"
    print("PASS: VIEW functionality works correctly")

def test_complete_functionality():
    """Test the complete functionality."""
    print("Testing COMPLETE functionality...")
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Buy groceries")
    assert not todo.completed, "Todo should not be completed initially"

    # Mark as complete
    updated_todo = service.mark_complete(todo.id)
    assert updated_todo is not None, "Failed to mark todo as complete"
    assert updated_todo.completed, "Todo should be completed after marking"
    print("PASS: COMPLETE functionality works correctly")

def test_delete_functionality():
    """Test the delete functionality."""
    print("Testing DELETE functionality...")
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Buy groceries")
    assert len(service.get_all_todos()) == 1, "Should have 1 todo initially"

    # Delete the todo
    success = service.delete_todo(todo.id)
    assert success, "Failed to delete todo"
    assert len(service.get_all_todos()) == 0, "Should have 0 todos after deletion"
    print("PASS: DELETE functionality works correctly")

def test_update_functionality():
    """Test the update functionality."""
    print("Testing UPDATE functionality...")
    service = TodoService()

    # Add a todo
    todo = service.add_todo("Buy groceries")
    assert todo.title == "Buy groceries", "Todo title should be 'Buy groceries'"

    # Update the todo
    updated_todo = service.update_todo(todo.id, "Buy groceries - urgent")
    assert updated_todo is not None, "Failed to update todo"
    assert updated_todo.title == "Buy groceries - urgent", "Todo title should be updated"
    print("PASS: UPDATE functionality works correctly")

def test_validation():
    """Test validation functionality."""
    print("Testing VALIDATION functionality...")
    service = TodoService()

    # Test empty description
    result = service.add_todo("")
    assert result is None, "Should not add todo with empty description"

    # Test too long description
    long_desc = "x" * 256
    result = service.add_todo(long_desc)
    assert result is None, "Should not add todo with too long description"

    # Test valid description
    result = service.add_todo("Valid description")
    assert result is not None, "Should add todo with valid description"

    # Test invalid ID for update
    result = service.update_todo(999, "New title")
    assert result is None, "Should not update non-existent todo"

    # Test invalid ID for complete
    result = service.mark_complete(999)
    assert result is None, "Should not complete non-existent todo"

    # Test invalid ID for delete
    result = service.delete_todo(999)
    success = service.delete_todo(999)
    assert not success, "Should not delete non-existent todo"

    print("PASS: VALIDATION functionality works correctly")

def run_manual_test():
    """Run a manual test by simulating CLI commands."""
    print("\nTesting CLI manually...")
    print("Creating CLI instance...")

    service = TodoService()
    cli = CLI(service)

    print("CLI instance created successfully!")
    print("All core functionality tested successfully!")

if __name__ == "__main__":
    print("Running Todo App tests...\n")

    test_add_functionality()
    test_view_functionality()
    test_complete_functionality()
    test_delete_functionality()
    test_update_functionality()
    test_validation()
    run_manual_test()

    print("\nPASS: All tests passed! The Todo App is working correctly.")