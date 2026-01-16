"""
TodoManager: Core business logic for task management.

This module handles all CRUD operations for tasks with in-memory storage.
No UI logic - pure business logic only.
"""

from datetime import datetime
from typing import Dict, List, Optional, Any


class TodoManager:
    """Manages todo tasks with in-memory storage."""
    
    def __init__(self):
        """Initialize empty task list and ID counter."""
        self._tasks: List[Dict[str, Any]] = []
        self._next_id: int = 1
    
    def add_task(self, title: str) -> Dict[str, Any]:
        """
        Add a new task with validation.
        
        Args:
            title: Task description (1-100 characters)
            
        Returns:
            Created task dictionary
            
        Raises:
            ValueError: If title is invalid (empty or too long)
        """
        # Validate title
        title = title.strip()
        
        if not title:
            raise ValueError("Task title cannot be empty")
        
        if len(title) > 100:
            raise ValueError("Task title too long (max 100 characters)")
        
        # Create task
        task = {
            "id": self._next_id,
            "title": title,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        
        # Add to list and increment ID
        self._tasks.append(task)
        self._next_id += 1
        
        return task
    
    def get_all_tasks(self) -> List[Dict[str, Any]]:
        """
        Get all tasks.
        
        Returns:
            Copy of task list (prevents external modification)
        """
        return self._tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Dict[str, Any]]:
        """
        Find task by ID.
        
        Args:
            task_id: Task identifier
            
        Returns:
            Task dictionary if found, None otherwise
        """
        for task in self._tasks:
            if task["id"] == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: str) -> bool:
        """
        Update task title.
        
        Args:
            task_id: Task identifier
            title: New title (1-100 characters)
            
        Returns:
            True if updated, False if task not found
            
        Raises:
            ValueError: If title is invalid
        """
        # Validate title
        title = title.strip()
        
        if not title:
            raise ValueError("Task title cannot be empty")
        
        if len(title) > 100:
            raise ValueError("Task title too long (max 100 characters)")
        
        # Find and update task
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        task["title"] = title
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete task by ID.
        
        Args:
            task_id: Task identifier
            
        Returns:
            True if deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        self._tasks.remove(task)
        return True
    
    def toggle_complete(self, task_id: int) -> bool:
        """
        Toggle task completion status.
        
        Args:
            task_id: Task identifier
            
        Returns:
            True if toggled, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        task["completed"] = not task["completed"]
        return True
    
    def get_task_count(self) -> int:
        """Get total number of tasks."""
        return len(self._tasks)
    
    def get_completed_count(self) -> int:
        """Get number of completed tasks."""
        return sum(1 for task in self._tasks if task["completed"])