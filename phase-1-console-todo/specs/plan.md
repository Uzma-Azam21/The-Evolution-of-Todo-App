# Architectural Plan: Console Todo Application

**Branch**: `001-console-todo-app` | **Date**: 2025-12-20 | **Spec**: [spec.md](./spec.md)  
**Input**: Feature specification from `phase-1-console-todo/specs/spec.md`

---

## Overview

Interactive Python console app for task management using in-memory storage. Menu-driven interface with CRUD operations and input validation.

---

## Technical Stack

**Language**: Python 3.10+  
**Dependencies**: None (pytest for testing)  
**Storage**: In-memory list  
**Testing**: pytest, 80%+ coverage  
**Platform**: Cross-platform console  
**Constraints**: No persistence, no external libraries, single-user  
**Performance**: <100ms operations, 1000+ tasks supported

---

## Constitution Validation

**GATE**: Must pass before implementation begins.

- ✅ Spec-Driven: Derived exclusively from spec.md
- ✅ Complete Coverage: All FR-001 to FR-009 addressed
- ✅ Phase Consistency: Foundation for Phase II web transition
- ✅ AI-Generated: Claude Code implementation only
- ✅ Reproducible: Traceable to specification requirements

---

## Code Organization

### Documentation
```
phase-1-console-todo/specs/
├── spec.md              # Requirements
├── plan.md              # This file
├── tasks.md             # Implementation checklist
├── research.md          # Technical research notes
├── data-model.md        # Data structure definitions
└── quickstart.md        # Setup and run guide
```

### Implementation
```
phase-1-console-todo/src/
├── main.py              # Entry point
├── todo_manager.py      # Core logic
└── ui.py                # Console interface

phase-1-console-todo/tests/
└── test_todo_manager.py # Unit tests
```

**Rationale**: Separation enables logic testing without UI, prepares for Phase II UI swap.

---

## Key Design Choices

### Choice 1: Module Separation Strategy
**Selected**: Three modules (main, logic, UI)  
**Alternatives Rejected**:
- Single file: Untestable, tight coupling
- Four layers with DAL: Over-engineering for in-memory list

**Justification**: Business logic must work independently for Phase II web integration.

---

### Choice 2: Data Storage Approach
**Selected**: `List[Dict]` with dictionaries as task records  
**Alternatives Rejected**:
- Dict with ID keys: Loses creation order
- Custom Task classes: Unnecessary complexity

**Justification**: Simple, maintains order, easy to serialize for Phase II.

---

### Choice 3: ID Generation Method
**Selected**: Auto-increment integers from 1, never reused  
**Alternatives Rejected**:
- UUID: User-hostile for CLI reference
- List indices: Break on deletion

**Justification**: Matches user mental model (displayed numbers).

---

### Choice 4: Timestamp Format
**Selected**: ISO 8601 strings (`YYYY-MM-DDTHH:MM:SS`)  
**Alternatives Rejected**:
- Unix epoch: Not human-readable
- datetime objects: Serialization issues

**Justification**: Standard format, Phase II API-ready.

---

## Architecture Sketch

### Data Flow
```
User Input → ui.py → todo_manager.py → In-Memory List
              ↓                ↓
         Validation      State Update
              ↓                ↓
         ui.py (display) ← Response
```

### Task Structure
```python
{
    "id": int,           # Sequential, starts at 1
    "title": str,        # 1-100 chars
    "completed": bool,   # Default False
    "created_at": str    # ISO 8601
}
```

### Module Responsibilities

**main.py**:
- Initialize TodoManager
- Start UI loop
- Handle clean exit

**todo_manager.py**:
- CRUD operations
- Input validation
- ID generation
- State management

**ui.py**:
- Menu display
- Input collection
- Output formatting
- Error messaging

---

## Validation Strategy

### Input Validation
- Menu: 1-6 only, reject others
- Task ID: Must exist, must be integer
- Task title: 1-100 chars, strip whitespace, reject empty

### Testing Approach
**Unit Tests** (todo_manager.py):
- Add task: valid, empty, too long
- Get task: valid ID, invalid ID
- Update: valid, invalid ID, bad title
- Delete: valid, invalid ID
- Toggle: valid, invalid ID
- ID generation sequence

**Coverage Target**: 85%+

**Integration Tests** (optional):
- Full user flows (add → view → complete → delete)

---

## Implementation Phases

### Phase 0: Setup
- Create file structure
- Configure pytest
- Write test scaffolding

### Phase 1: Core Logic
- Implement TodoManager class
- Write unit tests (TDD)
- Validate all edge cases

### Phase 2: User Interface
- Implement ui.py functions
- Menu loop logic
- Display formatting

### Phase 3: Integration
- Wire main.py
- End-to-end testing
- Error handling polish

**Estimated Time**: 2-3 hours

---

## Quality Checkpoints

- [ ] All spec requirements mapped to code
- [ ] Test coverage ≥80%
- [ ] No hardcoded values
- [ ] All errors handled gracefully
- [ ] Cross-platform tested (Windows/Mac/Linux)
- [ ] No external dependencies
- [ ] Data lost on exit (verified)

---

## Future Considerations

**Phase II Preparation**:
- TodoManager interface unchanged
- Swap ui.py for FastAPI endpoints
- Task dict → SQLModel ORM mapping

**Extension Points**:
- Add persistence layer without changing TodoManager
- Add new Task fields without breaking existing code

---
