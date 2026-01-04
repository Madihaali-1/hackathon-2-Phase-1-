# Implementation Plan: Phase I – In-Memory Python Console Todo App

**Feature**: 1-todo-app
**Created**: 2026-01-04
**Status**: Draft
**Input**: Architecture plan with entry point, domain model, in-memory store, services, CLI layer, and utils

## Technical Context

### Architecture Overview
- **Entry point**: main.py (CLI loop and command routing)
- **Domain model**: Todo (id, title, completed)
- **In-memory store**: List-based repository
- **Services**: TodoService (business logic)
- **CLI layer**: Input parsing and output rendering
- **Utils**: Validation and error handling

### Technology Stack
- **Language**: Python 3.13+
- **Package Manager**: UV
- **Dependencies**: Standard library only (no external packages)
- **Platform**: Console application
- **Data Storage**: In-memory only (no files or DB)

### Constraints
- No persistence or external dependencies
- Pure Python 3.13+, managed with UV
- Single-user, deterministic flow
- Console-only interface
- No external services or network dependencies

### Dependencies and Integrations
- **Python Standard Library**: Used for all functionality
- **UV Package Manager**: For dependency management
- **Console/Shell**: For user interaction

## Constitution Check

### Phase I Compliance
- [x] Language: Python only (✓)
- [x] No database, files, or external services (✓)
- [x] Data stored only in runtime memory (✓)
- [x] Single-user execution model (✓)
- [x] Console-based interaction only (✓)
- [x] Focus on core Todo logic and command handling (✓)

### Core Principles Verification
- [x] Simplicity First, Scalability Later: Starting with basic in-memory functionality
- [x] Clean Architecture and Separation of Concerns: Clear layer separation defined
- [x] Deterministic Behavior in Early Phases: No external dependencies
- [x] Extensibility for AI and Cloud-Native Integrations: Architecture supports future phases
- [x] Production-Grade Practices Phase-by-Phase: Following proper engineering practices
- [x] Phase Compliance and Constraint Adherence: Adheres to Phase I constraints

### Risk Assessment
- **Low Risk**: All functionality within Phase I constraints
- **No Violations**: Architecture aligns with constitutional requirements
- **No Blockers**: Can proceed with implementation

## Phase 0: Outline & Research

### Research Tasks

1. **Python 3.13+ Features Research**
   - Task: "Research Python 3.13+ features for console todo app implementation"
   - Need to identify any specific features of Python 3.13+ that could benefit this project

2. **CLI Best Practices Research**
   - Task: "Find best practices for CLI applications in Python using standard library"
   - Need to understand optimal approaches for command-line parsing and interaction

3. **Data Model Validation Research**
   - Task: "Research validation patterns for simple data models in Python"
   - Need to identify appropriate validation approaches for the Todo model

### Research Findings

**Decision**: Use dataclasses for Todo model with basic validation
**Rationale**: Dataclasses provide clean, readable code with built-in features, while validation can be implemented simply with properties
**Alternatives considered**: Named tuples (less flexible), regular classes (more verbose)

**Decision**: Use input() for user input and print() for output
**Rationale**: Standard library functions that meet console-only requirement without external dependencies
**Alternatives considered**: argparse (for complex commands), click library (requires external dependency)

**Decision**: Use UUID for ID generation or simple incrementing integers
**Rationale**: UUIDs provide guaranteed uniqueness, simple integers are easier to work with for CLI
**Alternatives considered**:
**Chosen**: Simple incrementing integers for ease of use in console interface

## Phase 1: Design & Contracts

### Data Model: data-model.md

#### Todo Entity
- **id**: int (unique identifier, auto-incremented)
- **title**: str (task description, required, 1-255 characters)
- **completed**: bool (completion status, default False)

#### Validation Rules
- Title must be between 1 and 255 characters
- ID must be a positive integer
- Completed field must be boolean

#### State Transitions
- Initial state: completed = False
- Transition to completed: completed = True (via mark_complete operation)

### API Contracts (CLI Commands)

#### Command Structure
```
todo <action> [parameters]
```

#### Available Commands
1. **add**: Add a new todo item
   - Syntax: `todo add "task description"`
   - Response: Confirmation with assigned ID

2. **view**: View all todo items
   - Syntax: `todo view`
   - Response: List of all todos with ID, title, and status

3. **update**: Update a todo description
   - Syntax: `todo update <id> "new description"`
   - Response: Confirmation of update

4. **delete**: Delete a todo item
   - Syntax: `todo delete <id>`
   - Response: Confirmation of deletion

5. **complete**: Mark a todo as complete
   - Syntax: `todo complete <id>`
   - Response: Confirmation of completion

6. **help**: Show available commands
   - Syntax: `todo help`
   - Response: Help text showing all commands

### Project Structure
```
todo-app/
├── main.py                 # Entry point with CLI loop
├── models/
│   └── todo.py            # Todo data model
├── repositories/
│   └── todo_repository.py # In-memory storage
├── services/
│   └── todo_service.py    # Business logic
├── cli/
│   └── cli.py             # Command parsing and output
├── utils/
│   └── validators.py      # Input validation
├── pyproject.toml         # Project dependencies
└── README.md              # Project documentation
```

### Quickstart Guide: quickstart.md

1. **Setup**:
   ```bash
   # Ensure Python 3.13+ is installed
   python --version

   # Install dependencies with UV
   uv sync
   ```

2. **Run the Application**:
   ```bash
   python main.py
   # or
   uv run main.py
   ```

3. **Usage Examples**:
   ```
   todo add "Buy groceries"
   todo view
   todo complete 1
   todo update 1 "Buy groceries - urgent"
   todo delete 1
   ```

## Implementation Steps

1. **Define Todo data model** - Create the Todo class with id, title, completed fields
2. **Implement in-memory repository** - Create TodoRepository with add, get, update, delete methods
3. **Implement core operations** - Create TodoService with business logic for all operations
4. **Build CLI command loop** - Create CLI interface to handle commands and user interaction
5. **Add input validation and user feedback** - Add validation and proper error handling
6. **Final manual test via console** - Test all functionality end-to-end

## Architecture Decisions

1. **Layered Architecture**: Clear separation between models, repositories, services, and CLI
2. **In-Memory Storage**: Using Python list/dict for temporary storage during execution
3. **Synchronous Operations**: Simple synchronous operations appropriate for single-user console app
4. **Standard Library Only**: Avoiding external dependencies to meet constraints

## Agent Context Update

The following technologies and patterns will be added to the agent context:
- Python dataclasses for models
- In-memory list/dict storage patterns
- CLI input/output handling
- Input validation techniques
- Service layer pattern for business logic