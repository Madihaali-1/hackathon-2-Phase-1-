# Data Model: Todo Entity

## Todo Entity

### Attributes
- **id**: int (unique identifier, auto-incremented)
- **title**: str (task description, required, 1-255 characters)
- **completed**: bool (completion status, default False)

### Validation Rules
- Title must be between 1 and 255 characters
- ID must be a positive integer
- Completed field must be boolean

### State Transitions
- Initial state: completed = False
- Transition to completed: completed = True (via mark_complete operation)

## Relationships
- No relationships needed for this simple entity

## Constraints
- Each todo must have a unique ID
- Title cannot be empty
- Title must not exceed 255 characters
- Completed status can only be True or False