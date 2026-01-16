# Data Structures: Console Todo Application

**Date**: 2025-12-20

This document defines the data entities and their structure for the console todo application.

---

## Task Entity

The `Task` represents a single todo item in the application.

### Fields

- **id** (`int`): Unique sequential identifier. Auto-assigned starting from 1.
- **title** (`str`): The task description text.
- **completed** (`bool`): Indicates whether the task is done. Defaults to `False`.
- **created_at** (`str`): ISO 8601 timestamp of when the task was created.

### Validation Constraints

- `title` must be between 1-100 characters
- `title` cannot be empty or whitespace-only
- `id` is immutable after creation

### Example Instance

```python
{
    "id": 1,
    "title": "Buy groceries",
    "completed": False,
    "created_at": "2025-01-12T10:30:00"
}
```

---

## Storage Structure

Tasks are stored in a Python list during runtime:

```python
tasks: List[Dict[str, Any]] = []
```

**Characteristics**:
- In-memory only (no file/database)
- Maintains insertion order
- Data cleared on application exit