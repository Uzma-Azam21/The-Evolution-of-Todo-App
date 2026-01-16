# Feature Specification: Console Todo App

**Feature**: `001-console-todo-app` | **Phase**: I | **Status**: Draft  
**Created**: 2025-12-20

**Input**: "Interactive menu-driven Python console app for task management. In-memory storage, no persistence. Operations: Add, View, Update, Delete, Toggle Complete. Clean separation of UI and logic. Input validation. Python 3.10+, pytest testing. Constraints: Console-only, single-user, offline. No file/DB, no GUI, no auth. Implementation via Claude Code only."

---

## User Scenarios *(mandatory)*

### US-1: Add Tasks (P0)
**As a** user, **I want to** add tasks via menu, **So that** I can capture todos quickly.

**Acceptance**:
1. Select "Add Task", enter "Buy groceries" → Task stored with ID and timestamp
2. Enter empty string → Error: "Task title cannot be empty"
3. Enter 101+ characters → Error: "Task title too long (max 100 characters)"

### US-2: View Tasks (P0)
**As a** user, **I want to** view all tasks with status, **So that** I see what needs doing.

**Acceptance**:
1. Have 3 tasks (2 incomplete, 1 complete) → See all with `[✓]` and `[ ]` markers
2. No tasks → Message: "No tasks yet. Add your first task!"
3. View shows: ID, status, title, timestamp (YYYY-MM-DD HH:MM)

### US-3: Update Tasks (P1)
**As a** user, **I want to** update task titles, **So that** tasks stay accurate.

**Acceptance**:
1. Update task ID 1 from "Buy milk" to "Buy milk and bread" → Title changes, ID/status preserved
2. Update invalid ID → Error: "Task not found"
3. Enter empty title → Error, update cancelled

### US-4: Delete Tasks (P1)
**As a** user, **I want to** delete tasks with confirmation, **So that** I avoid accidents.

**Acceptance**:
1. Delete task ID 2, confirm 'y' → Task removed
2. Respond 'n' to confirmation → Deletion cancelled
3. Delete invalid ID → Error: "Task not found"

### US-5: Toggle Complete (P0)
**As a** user, **I want to** mark tasks complete/incomplete, **So that** I track progress.

**Acceptance**:
1. Mark incomplete task complete → Displays `[✓]`
2. Toggle complete task → Becomes incomplete `[ ]`
3. Toggle invalid ID → Error: "Task not found"

### US-6: Exit (P2)
**As a** user, **I want to** exit cleanly, **So that** I know session ended.

**Acceptance**:
1. Select "Exit" → Message: "Goodbye! Your tasks will not be saved." + exit code 0

---

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: Interactive menu (1=Add, 2=View, 3=Update, 4=Delete, 5=Toggle, 6=Exit)
- **FR-002**: Input validation: menu 1-6, valid task IDs, titles 1-100 chars
- **FR-003**: Auto-assign sequential IDs starting from 1
- **FR-004**: In-memory storage only (Python list/dict)
- **FR-005**: Display format: ID, status (`[✓]`/`[ ]`), title, timestamp
- **FR-006**: ISO 8601 timestamps (YYYY-MM-DDTHH:MM:SS)
- **FR-007**: Delete requires y/n confirmation
- **FR-008**: Clear error messages for all failures
- **FR-009**: Return to menu after each operation

### Key Entities
**Task**: `{id: int, title: str, completed: bool, created_at: str}`  
**TodoManager**: CRUD operations, ID generation, validation  
**UI**: Menu display, input collection, output formatting

---

## Success Criteria *(mandatory)*
- **SC-001**: All CRUD operations functional via menu
- **SC-002**: 80%+ test coverage, logic testable without UI
- **SC-003**: Python 3.10+, stdlib only (pytest for tests)
- **SC-004**: All invalid inputs handled without crashes
- **SC-005**: Data lost on exit (no persistence)
- **SC-006**: Separation: main.py, todo_manager.py, ui.py, tests/
- **SC-007**: <100ms response with 1000 tasks
- **SC-008**: Cross-platform (Windows, macOS, Linux)

---

## Assumptions
- **A-001**: Numbered menu (1-6) navigation
- **A-002**: Sequential IDs, never reused in session
- **A-003**: Standard Python project structure
- **A-004**: Text input only (Enter to submit)
- **A-005**: UTF-8 encoding, English text

---

## Out of Scope
File/DB persistence, Web/GUI, Multi-user, Task metadata (priority/dates/categories), Search/filter, Sorting, History, Undo/redo, Auth, Network, External libraries

---
