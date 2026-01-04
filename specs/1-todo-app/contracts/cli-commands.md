# CLI Command Contracts: Todo App

## Command Format
```
todo <action> [parameters]
```

## Available Commands

### 1. Add Todo
- **Command**: `todo add "<description>"`
- **Parameters**:
  - description: string (required, 1-255 characters)
- **Response**:
  - Success: "Todo added with ID: {id}"
  - Error: "Error: {error_message}"
- **Example**: `todo add "Buy groceries"`

### 2. View Todos
- **Command**: `todo view`
- **Parameters**: None
- **Response**:
  - Success: List of todos in format "ID: [id] | [completed] | [title]"
  - Empty: "No todos found"
  - Error: "Error: {error_message}"
- **Example**: `todo view`

### 3. Update Todo
- **Command**: `todo update <id> "<new_description>"`
- **Parameters**:
  - id: integer (required, positive)
  - new_description: string (required, 1-255 characters)
- **Response**:
  - Success: "Todo {id} updated successfully"
  - Error: "Error: {error_message}"
- **Example**: `todo update 1 "Buy groceries - urgent"`

### 4. Delete Todo
- **Command**: `todo delete <id>`
- **Parameters**:
  - id: integer (required, positive)
- **Response**:
  - Success: "Todo {id} deleted successfully"
  - Error: "Error: {error_message}"
- **Example**: `todo delete 1`

### 5. Mark Complete
- **Command**: `todo complete <id>`
- **Parameters**:
  - id: integer (required, positive)
- **Response**:
  - Success: "Todo {id} marked as complete"
  - Error: "Error: {error_message}"
- **Example**: `todo complete 1`

### 6. Help
- **Command**: `todo help`
- **Parameters**: None
- **Response**: Help text showing all available commands
- **Example**: `todo help`

## Error Responses
- Invalid command: "Error: Unknown command '{command}'. Use 'todo help' for available commands."
- Invalid ID: "Error: Todo with ID {id} does not exist."
- Invalid description: "Error: Description must be 1-255 characters long."
- Invalid syntax: "Error: Invalid command syntax. Use 'todo help' for usage information."