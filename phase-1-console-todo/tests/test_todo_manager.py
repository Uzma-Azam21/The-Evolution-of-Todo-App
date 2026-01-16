"""
Unit tests for TodoManager business logic.

Tests all CRUD operations, validation, and edge cases.
"""

import pytest
import sys
sys.path.insert(0, '../src')

from todo_manager import TodoManager


# Initialization Tests

def test_init_creates_empty_list():
    """TodoManager initializes with empty task list."""
    manager = TodoManager()
    assert manager.get_all_tasks() == []


def test_init_sets_first_id_to_one():
    """TodoManager sets first ID to 1."""
    manager = TodoManager()
    task = manager.add_task("First task")
    assert task["id"] == 1


# Add Task Tests

def test_add_task_with_valid_title():
    """Add task with valid title creates task correctly."""
    manager = TodoManager()
    task = manager.add_task("Buy milk")
    
    assert task["id"] == 1
    assert task["title"] == "Buy milk"
    assert task["completed"] is False
    assert "created_at" in task


def test_add_task_increments_id():
    """Multiple tasks get sequential IDs."""
    manager = TodoManager()
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")
    task3 = manager.add_task("Task 3")
    
    assert task1["id"] == 1
    assert task2["id"] == 2
    assert task3["id"] == 3


def test_add_task_empty_title_raises_error():
    """Adding task with empty title raises ValueError."""
    manager = TodoManager()
    with pytest.raises(ValueError, match="cannot be empty"):
        manager.add_task("")


def test_add_task_whitespace_only_raises_error():
    """Adding task with only whitespace raises ValueError."""
    manager = TodoManager()
    with pytest.raises(ValueError, match="cannot be empty"):
        manager.add_task("   ")


def test_add_task_too_long_raises_error():
    """Adding task with >100 chars raises ValueError."""
    manager = TodoManager()
    long_title = "x" * 101
    with pytest.raises(ValueError, match="too long"):
        manager.add_task(long_title)


def test_add_task_trims_whitespace():
    """Adding task trims leading/trailing whitespace."""
    manager = TodoManager()
    task = manager.add_task("  Task with spaces  ")
    assert task["title"] == "Task with spaces"


def test_add_task_100_chars_accepted():
    """Task with exactly 100 chars is accepted."""
    manager = TodoManager()
    title = "x" * 100
    task = manager.add_task(title)
    assert task["title"] == title


# Get Tasks Tests

def test_get_all_tasks_empty():
    """get_all_tasks returns empty list when no tasks."""
    manager = TodoManager()
    assert manager.get_all_tasks() == []


def test_get_all_tasks_returns_all():
    """get_all_tasks returns all added tasks."""
    manager = TodoManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    
    tasks = manager.get_all_tasks()
    assert len(tasks) == 2


def test_get_all_tasks_returns_copy():
    """get_all_tasks returns copy, not original list."""
    manager = TodoManager()
    manager.add_task("Task 1")
    
    tasks1 = manager.get_all_tasks()
    tasks2 = manager.get_all_tasks()
    
    assert tasks1 is not tasks2


def test_get_task_by_id_valid():
    """get_task_by_id returns correct task."""
    manager = TodoManager()
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")
    
    found = manager.get_task_by_id(2)
    assert found["id"] == 2
    assert found["title"] == "Task 2"


def test_get_task_by_id_invalid_returns_none():
    """get_task_by_id returns None for non-existent ID."""
    manager = TodoManager()
    manager.add_task("Task 1")
    
    found = manager.get_task_by_id(999)
    assert found is None


# Update Task Tests

def test_update_task_valid():
    """update_task changes title correctly."""
    manager = TodoManager()
    task = manager.add_task("Old title")
    
    result = manager.update_task(1, "New title")
    
    assert result is True
    updated = manager.get_task_by_id(1)
    assert updated["title"] == "New title"


def test_update_task_preserves_other_fields():
    """update_task doesn't change ID, completed, or created_at."""
    manager = TodoManager()
    task = manager.add_task("Original")
    manager.toggle_complete(1)
    
    original_id = task["id"]
    original_created = task["created_at"]
    
    manager.update_task(1, "Updated")
    
    updated = manager.get_task_by_id(1)
    assert updated["id"] == original_id
    assert updated["completed"] is True
    assert updated["created_at"] == original_created


def test_update_task_invalid_id_returns_false():
    """update_task returns False for non-existent ID."""
    manager = TodoManager()
    result = manager.update_task(999, "New title")
    assert result is False


def test_update_task_empty_title_raises_error():
    """update_task raises ValueError for empty title."""
    manager = TodoManager()
    manager.add_task("Task 1")
    
    with pytest.raises(ValueError, match="cannot be empty"):
        manager.update_task(1, "")


def test_update_task_too_long_raises_error():
    """update_task raises ValueError for >100 char title."""
    manager = TodoManager()
    manager.add_task("Task 1")
    
    with pytest.raises(ValueError, match="too long"):
        manager.update_task(1, "x" * 101)


# Delete Task Tests

def test_delete_task_valid():
    """delete_task removes task correctly."""
    manager = TodoManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    
    result = manager.delete_task(1)
    
    assert result is True
    assert len(manager.get_all_tasks()) == 1
    assert manager.get_task_by_id(1) is None


def test_delete_task_invalid_id_returns_false():
    """delete_task returns False for non-existent ID."""
    manager = TodoManager()
    result = manager.delete_task(999)
    assert result is False


def test_delete_task_preserves_other_ids():
    """Deleting task doesn't change IDs of remaining tasks."""
    manager = TodoManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.add_task("Task 3")
    
    manager.delete_task(2)
    
    assert manager.get_task_by_id(1) is not None
    assert manager.get_task_by_id(3) is not None


# Toggle Complete Tests

def test_toggle_complete_marks_incomplete_as_complete():
    """toggle_complete changes False to True."""
    manager = TodoManager()
    manager.add_task("Task 1")
    
    result = manager.toggle_complete(1)
    
    assert result is True
    task = manager.get_task_by_id(1)
    assert task["completed"] is True


def test_toggle_complete_marks_complete_as_incomplete():
    """toggle_complete changes True to False."""
    manager = TodoManager()
    manager.add_task("Task 1")
    manager.toggle_complete(1)  # Make it complete
    
    result = manager.toggle_complete(1)  # Toggle back
    
    assert result is True
    task = manager.get_task_by_id(1)
    assert task["completed"] is False


def test_toggle_complete_invalid_id_returns_false():
    """toggle_complete returns False for non-existent ID."""
    manager = TodoManager()
    result = manager.toggle_complete(999)
    assert result is False


def test_toggle_complete_preserves_other_fields():
    """toggle_complete doesn't change title, ID, or timestamp."""
    manager = TodoManager()
    task = manager.add_task("Task 1")
    
    original_id = task["id"]
    original_title = task["title"]
    original_created = task["created_at"]
    
    manager.toggle_complete(1)
    
    updated = manager.get_task_by_id(1)
    assert updated["id"] == original_id
    assert updated["title"] == original_title
    assert updated["created_at"] == original_created


# Count Tests

def test_get_task_count_empty():
    """get_task_count returns 0 for empty list."""
    manager = TodoManager()
    assert manager.get_task_count() == 0


def test_get_task_count_after_adds():
    """get_task_count returns correct count."""
    manager = TodoManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    assert manager.get_task_count() == 2


def test_get_completed_count_none_complete():
    """get_completed_count returns 0 when none complete."""
    manager = TodoManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    assert manager.get_completed_count() == 0


def test_get_completed_count_some_complete():
    """get_completed_count returns correct count."""
    manager = TodoManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    manager.add_task("Task 3")
    
    manager.toggle_complete(1)
    manager.toggle_complete(3)
    
    assert manager.get_completed_count() == 2