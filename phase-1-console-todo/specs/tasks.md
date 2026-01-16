# Implementation Tasks: Console Todo Application

**Input**: Design specifications from `phase-1-console-todo/specs/`  
**Prerequisites**: spec.md, plan.md, data-model.md  
**Date**: 2025-12-20

---

## Phase 0: Foundation Setup

**Goal**: Establish project structure and development environment.

- [ ] **T001** - Create directory structure: `src/`, `tests/`
- [ ] **T002** - Initialize Python package files: `src/__init__.py`, `tests/__init__.py`
- [ ] **T003** - Create module stubs from plan.md: `src/main.py`, `src/todo_manager.py`, `src/ui.py`
- [ ] **T004** - Create test file: `tests/test_todo_manager.py`
- [ ] **T005** - Configure `requirements.txt` with pytest dependency
- [ ] **T006** - Setup `.gitignore` for Python artifacts

**Validation**: Directory structure matches plan.md, Python imports work without errors

---

## Phase 1: Core Logic Layer

**Goal**: Implement business logic with comprehensive test coverage (TDD approach).

### TodoManager Class Foundation

- [ ] **T101** - Implement `TodoManager.__init__()` with empty task list and ID counter
- [ ] **T102** - Write tests for initialization state (empty list, ID starts at 1)

### Add Task Feature (US-1)

- [ ] **T103** - [US1] Write test: `test_add_task_with_valid_title()`
- [ ] **T104** - [US1] Write test: `test_add_task_empty_title_raises_error()`
- [ ] **T105** - [US1] Write test: `test_add_task_long_title_raises_error()`
- [ ] **T106** - [US1] Write test: `test_add_task_whitespace_handling()`
- [ ] **T107** - [US1] Implement `TodoManager.add_task(title)` to pass all tests
- [ ] **T108** - [US1] Verify ID auto-increment works correctly

### View Tasks Feature (US-2)

- [ ] **T109** - [US2] Write test: `test_get_all_tasks_empty_list()`
- [ ] **T110** - [US2] Write test: `test_get_all_tasks_returns_copy()`
- [ ] **T111** - [US2] Write test: `test_get_task_by_id_valid()`
- [ ] **T112** - [US2] Write test: `test_get_task_by_id_invalid_returns_none()`
- [ ] **T113** - [US2] Implement `TodoManager.get_all_tasks()`
- [ ] **T114** - [US2] Implement `TodoManager.get_task_by_id(task_id)`

### Toggle Complete Feature (US-5)

- [ ] **T115** - [US5] Write test: `test_toggle_complete_marks_incomplete_as_complete()`
- [ ] **T116** - [US5] Write test: `test_toggle_complete_marks_complete_as_incomplete()`
- [ ] **T117** - [US5] Write test: `test_toggle_complete_invalid_id_returns_false()`
- [ ] **T118** - [US5] Implement `TodoManager.toggle_complete(task_id)`

---

## Phase 2: Secondary Operations

**Goal**: Implement update and delete functionality.

### Update Task Feature (US-3)

- [ ] **T201** - [US3] Write test: `test_update_task_valid_id_and_title()`
- [ ] **T202** - [US3] Write test: `test_update_task_invalid_id_returns_false()`
- [ ] **T203** - [US3] Write test: `test_update_task_empty_title_raises_error()`
- [ ] **T204** - [US3] Write test: `test_update_task_preserves_other_fields()`
- [ ] **T205** - [US3] Implement `TodoManager.update_task(task_id, title)`

### Delete Task Feature (US-4)

- [ ] **T206** - [US4] Write test: `test_delete_task_valid_id()`
- [ ] **T207** - [US4] Write test: `test_delete_task_invalid_id_returns_false()`
- [ ] **T208** - [US4] Write test: `test_delete_task_preserves_other_ids()`
- [ ] **T209** - [US4] Implement `TodoManager.delete_task(task_id)`

---

## Phase 3: User Interface Layer

**Goal**: Build console interface for user interaction.

### Menu System

- [ ] **T301** - Implement `ui.display_menu(task_count, completed_count)`
- [ ] **T302** - Implement `ui.get_menu_choice()` with validation (1-6 only)
- [ ] **T303** - Implement `ui.clear_screen()` for cross-platform support

### Task Display

- [ ] **T304** - Implement `ui.display_tasks(tasks)` with formatting
- [ ] **T305** - Implement status markers: `[✓]` for complete, `[ ]` for incomplete
- [ ] **T306** - Implement timestamp formatting (YYYY-MM-DD HH:MM)

### Input Collection

- [ ] **T307** - Implement `ui.get_task_input()` for task title entry
- [ ] **T308** - Implement `ui.get_task_id()` for ID entry with validation
- [ ] **T309** - Implement `ui.confirm_action(prompt)` for y/n confirmations

### Feedback Display

- [ ] **T310** - Implement `ui.show_success(message)` with ✓ prefix
- [ ] **T311** - Implement `ui.show_error(message)` with ❌ prefix
- [ ] **T312** - Implement pause mechanism ("Press Enter to continue...")

---

## Phase 4: Application Integration

**Goal**: Wire all components together into working application.

### Main Application Loop

- [ ] **T401** - Implement `main.py` entry point with TodoManager initialization
- [ ] **T402** - Implement infinite menu loop with exit condition
- [ ] **T403** - Connect menu option 1 (Add) to UI and TodoManager
- [ ] **T404** - Connect menu option 2 (View) to UI and TodoManager
- [ ] **T405** - Connect menu option 3 (Update) to UI and TodoManager
- [ ] **T406** - Connect menu option 4 (Delete) to UI and TodoManager
- [ ] **T407** - Connect menu option 5 (Toggle) to UI and TodoManager
- [ ] **T408** - Connect menu option 6 (Exit) with goodbye message

### Error Handling Integration

- [ ] **T409** - Wrap TodoManager calls in try-except blocks
- [ ] **T410** - Display appropriate error messages via ui.show_error()
- [ ] **T411** - Handle keyboard interrupts (Ctrl+C) gracefully

---

## Phase 5: Testing & Validation

**Goal**: Ensure complete test coverage and validation.

### Unit Testing

- [ ] **T501** - Run all TodoManager tests, verify 90%+ coverage
- [ ] **T502** - Add edge case tests for boundary conditions
- [ ] **T503** - Test timestamp format validation

### Integration Testing

- [ ] **T504** - Test complete add → view → complete → delete flow
- [ ] **T505** - Test error handling end-to-end
- [ ] **T506** - Test menu navigation with invalid inputs

### Manual Validation

- [ ] **T507** - Follow quickstart.md instructions exactly
- [ ] **T508** - Verify all 6 menu options work correctly
- [ ] **T509** - Test on Windows, macOS, and Linux (if possible)
- [ ] **T510** - Verify data is lost on exit (no persistence)

---

## Phase 6: Documentation & Cleanup

**Goal**: Finalize documentation and prepare for handoff.

- [ ] **T601** - Update quickstart.md with any discovered issues
- [ ] **T602** - Create phase-1-console-todo/README.md with overview
- [ ] **T603** - Verify all spec requirements met (checklist/requirements.md)
- [ ] **T604** - Create sample PHR files in history/prompts/
- [ ] **T605** - Clean up any debug code or comments
- [ ] **T606** - Final test run with coverage report

---

## Execution Strategy

**Sequential Dependencies**:
1. Phase 0 must complete before any other phase
2. Phase 1 (Core Logic) must complete before Phase 3 (UI)
3. Phase 2 (Secondary Ops) can run parallel to Phase 3
4. Phase 4 (Integration) requires Phases 1, 2, and 3 complete
5. Phase 5 (Testing) follows Phase 4
6. Phase 6 (Documentation) is final step

**Parallel Work Opportunities**:
- Phase 2 and Phase 3 can be developed simultaneously
- Test writing and implementation can happen in TDD cycles

**Critical Path**: Phase 0 → Phase 1 → Phase 4 → Phase 5 → Phase 6

---

