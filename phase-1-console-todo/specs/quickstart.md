# Quick Start: Console Todo Application

**Date**: 2025-12-20

Instructions for running the console todo application.

---

## Prerequisites

- Python 3.10 or higher installed
- Terminal or command prompt access

**Verify Python installation**:
```bash
python --version
```

---

## Setup Steps

1. **Navigate to the project directory**:
   ```bash
   cd phase-1-console-todo
   ```

2. **Install test dependencies** (optional, for running tests):
   ```bash
   pip install pytest
   ```

---

## Running the Application

Execute the main script:
```bash
python src/main.py
```

The interactive menu will appear with 6 options:
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

---

## Running Tests

To verify the implementation:
```bash
pytest tests/
```

For coverage report:
```bash
pytest --cov=src tests/
```

---

## Important Notes

- All data is stored in memory only
- Tasks are lost when the application exits
- No configuration or setup files are required
- The application works on Windows, macOS, and Linux