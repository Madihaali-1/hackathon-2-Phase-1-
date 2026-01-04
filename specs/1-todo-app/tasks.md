# Implementation Tasks: Phase I – In-Memory Python Console Todo App

**Feature**: 1-todo-app
**Created**: 2026-01-04
**Status**: Draft

## Implementation Strategy

This implementation follows a progressive enhancement approach with clear phases:
1. Setup phase: Project initialization and basic structure
2. Foundational phase: Core data models and repository
3. User story phases: Implement functionality in priority order (P1, P2, P3...)
4. Polish phase: Cross-cutting concerns and final touches

The implementation delivers an MVP with just User Story 1 (Add New Todo) initially, then builds incrementally to include all functionality.

## Phase 1: Setup

**Goal**: Initialize project structure and dependencies

- [X] T001 Create project directory structure (models/, repositories/, services/, cli/, utils/, tests/)
- [X] T002 Create pyproject.toml with Python 3.13+ requirement and UV configuration
- [X] T003 Create README.md with project description and usage instructions
- [X] T004 [P] Create main.py entry point file
- [X] T005 [P] Create models/__init__.py file
- [X] T006 [P] Create repositories/__init__.py file
- [X] T007 [P] Create services/__init__.py file
- [X] T008 [P] Create cli/__init__.py file
- [X] T009 [P] Create utils/__init__.py file

## Phase 2: Foundational Components

**Goal**: Implement core data models and in-memory repository

- [X] T010 [P] Create Todo data model in models/todo.py with id, title, completed attributes
- [X] T011 [P] Implement Todo validation rules in models/todo.py (title length, id positivity, boolean status)
- [X] T012 [P] Create TodoRepository in repositories/todo_repository.py with in-memory storage
- [X] T013 [P] Implement add() method in TodoRepository to add new todos with auto-incremented IDs
- [X] T014 [P] Implement get_all() method in TodoRepository to retrieve all todos
- [X] T015 [P] Implement get_by_id() method in TodoRepository to retrieve a specific todo
- [X] T016 [P] Implement update() method in TodoRepository to update todo details
- [X] T017 [P] Implement delete() method in TodoRepository to remove a todo
- [X] T018 [P] Create validators utility in utils/validators.py with description validation

## Phase 3: User Story 1 - Add New Todo (Priority: P1)

**Goal**: Enable users to add new todo items to their list

**Independent Test**: User can run the command-line application and successfully add a new todo item with a description. The system stores the item in memory and confirms the addition.

**Acceptance Scenarios**:
1. Given the todo app is running, When user enters "add 'Buy groceries'", Then the task "Buy groceries" is added to the todo list and a confirmation message is displayed
2. Given the todo app is running, When user enters "add 'Complete project'", Then the task "Complete project" is added to the todo list with a unique identifier

- [X] T019 [P] [US1] Create TodoService in services/todo_service.py
- [X] T020 [US1] Implement add_todo() method in TodoService with validation
- [X] T021 [P] [US1] Create CLI command parsing in cli/cli.py
- [X] T022 [US1] Implement add command handler in CLI layer
- [X] T023 [US1] Integrate add functionality from service to CLI
- [X] T024 [US1] Add success response "Todo added with ID: {id}" for add command
- [X] T025 [US1] Add error handling for invalid descriptions in add command

## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Enable users to view their current todo list

**Independent Test**: User can run the command-line application and view all current todo items with their status (complete/incomplete).

**Acceptance Scenarios**:
1. Given there are multiple todo items in the list, When user enters "view", Then all todo items are displayed with their status and identifiers
2. Given there are no todo items in the list, When user enters "view", Then an appropriate message is displayed indicating the list is empty

- [X] T026 [P] [US2] Implement get_all_todos() method in TodoService
- [X] T027 [US2] Implement view command handler in CLI layer
- [X] T028 [US2] Format output as "ID: [id] | [completed] | [title]" for view command
- [X] T029 [US2] Handle empty list case with "No todos found" message
- [X] T030 [US2] Integrate view functionality from service to CLI

## Phase 5: User Story 3 - Mark Todo Complete (Priority: P2)

**Goal**: Enable users to mark todo items as complete

**Independent Test**: User can select a specific todo item and mark it as complete, with the system updating the status in memory.

**Acceptance Scenarios**:
1. Given there are pending todo items in the list, When user enters "complete 1", Then the todo item with ID 1 is marked as complete and the status is updated
2. Given a todo item exists, When user marks it as complete, Then the task remains in the list but shows as completed

- [X] T031 [P] [US3] Implement mark_complete() method in TodoService
- [X] T032 [US3] Implement complete command handler in CLI layer
- [X] T033 [US3] Add success response "Todo {id} marked as complete" for complete command
- [X] T034 [US3] Add error handling for non-existent todo IDs in complete command
- [X] T035 [US3] Integrate mark complete functionality from service to CLI

## Phase 6: User Story 4 - Delete Todo (Priority: P2)

**Goal**: Enable users to delete todo items from their list

**Independent Test**: User can select a specific todo item and delete it from the list.

**Acceptance Scenarios**:
1. Given there are todo items in the list, When user enters "delete 1", Then the todo item with ID 1 is removed from the list
2. Given a todo item is selected for deletion, When user confirms deletion, Then the item is permanently removed from memory

- [X] T036 [P] [US4] Implement delete_todo() method in TodoService
- [X] T037 [US4] Implement delete command handler in CLI layer
- [X] T038 [US4] Add success response "Todo {id} deleted successfully" for delete command
- [X] T039 [US4] Add error handling for non-existent todo IDs in delete command
- [X] T040 [US4] Integrate delete functionality from service to CLI

## Phase 7: User Story 5 - Update Todo Description (Priority: P3)

**Goal**: Enable users to update the description of existing todo items

**Independent Test**: User can select a specific todo item and update its description.

**Acceptance Scenarios**:
1. Given a todo item exists in the list, When user enters "update 1 'Buy groceries - urgent'", Then the description of the todo item with ID 1 is updated

- [X] T041 [P] [US5] Implement update_todo() method in TodoService
- [X] T042 [US5] Implement update command handler in CLI layer
- [X] T043 [US5] Add success response "Todo {id} updated successfully" for update command
- [X] T044 [US5] Add error handling for non-existent todo IDs in update command
- [X] T045 [US5] Add validation for updated description length in update command
- [X] T046 [US5] Integrate update functionality from service to CLI

## Phase 8: CLI Command Enhancement & Error Handling

**Goal**: Implement help command and comprehensive error handling

- [X] T047 [P] Implement help command handler in CLI layer
- [X] T048 [P] Add help response with all available commands and usage information
- [X] T049 [P] Implement generic error handling for invalid commands
- [X] T050 [P] Add error response for unknown commands: "Error: Unknown command '{command}'. Use 'todo help' for available commands."
- [X] T051 [P] Add error response for invalid IDs: "Error: Todo with ID {id} does not exist."
- [X] T052 [P] Add error response for invalid descriptions: "Error: Description must be 1-255 characters long."
- [X] T053 [P] Add error response for invalid syntax: "Error: Invalid command syntax. Use 'todo help' for usage information."

## Phase 9: Main Application Integration

**Goal**: Integrate all components into a cohesive CLI application

- [X] T054 [P] Initialize TodoService in main.py
- [X] T055 [P] Set up command loop in main.py to continuously accept user commands
- [X] T056 [P] Parse command-line arguments in main.py to route to appropriate CLI handlers
- [X] T057 [P] Implement graceful exit functionality (e.g., "quit" or "exit" command)
- [X] T058 [P] Add welcome message when application starts

## Phase 10: Polish & Cross-Cutting Concerns

**Goal**: Final touches and quality improvements

- [X] T059 [P] Add comprehensive docstrings to all classes and methods
- [X] T060 [P] Add type hints to all functions and methods
- [X] T061 [P] Clean up and organize imports across all modules
- [X] T062 [P] Implement consistent logging approach
- [X] T063 [P] Add input sanitization where needed
- [X] T064 [P] Add final integration tests to verify all functionality works together
- [X] T065 [P] Update README.md with complete usage instructions
- [X] T066 [P] Add error handling documentation to README.md

## Dependencies

User stories should be completed in this order:
1. User Story 1 (Add New Todo) - Foundation for all other functionality
2. User Story 2 (View Todo List) - Needed to verify other operations
3. User Story 3 (Mark Todo Complete) - Independent of others
4. User Story 4 (Delete Todo) - Independent of others
5. User Story 5 (Update Todo Description) - Independent of others

## Parallel Execution Examples

Per User Story:
- **US1**: Tasks T019-T025 can be developed in parallel with proper interface contracts
- **US2**: Tasks T026-T030 can be developed in parallel once repository is available
- **US3**: Tasks T031-T035 can be developed in parallel once core infrastructure exists
- **US4**: Tasks T036-T040 can be developed in parallel once core infrastructure exists
- **US5**: Tasks T041-T046 can be developed in parallel once core infrastructure exists

Cross-cutting:
- Tasks T047-T052 can be developed in parallel with user story implementation
- Tasks T059-T066 can be done after all user stories are complete

## MVP Scope

The MVP includes just User Story 1 (Add New Todo) functionality:
- Tasks T001-T025 provide a working application that allows users to add todos
- This delivers core value while maintaining simplicity
- Additional functionality can be added incrementally