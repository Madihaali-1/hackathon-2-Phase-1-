# Quickstart Guide: Phase I In-Memory Python Console Todo App

## Setup

1. **Ensure Python 3.13+ is installed**:
   ```bash
   python --version
   ```

2. **Install dependencies with UV**:
   ```bash
   uv sync
   ```

## Run the Application

```bash
# Run directly with Python
python main.py

# Or run with UV
uv run main.py
```

## Usage Examples

Once the application is running, you can use the following commands:

```
# Add a new todo
todo add "Buy groceries"

# View all todos
todo view

# Mark a todo as complete (use the ID from the view command)
todo complete 1

# Update a todo description
todo update 1 "Buy groceries - urgent"

# Delete a todo
todo delete 1

# Show help
todo help
```

## Expected Output

- **Add**: "Todo added with ID: 1"
- **View**: Lists all todos with their ID, status, and description
- **Complete**: "Todo 1 marked as complete"
- **Update**: "Todo 1 updated successfully"
- **Delete**: "Todo 1 deleted successfully"
- **Help**: Shows available commands and usage

## Error Handling

The application will show appropriate error messages for:
- Invalid commands
- Non-existent todo IDs
- Empty or too-long descriptions
- Malformed command syntax