"""
UI: Console user interface for todo application.

Handles display, input collection, and formatting.
No business logic - delegates to TodoManager.
"""

import os
from typing import List, Dict, Any
from todo_manager import TodoManager


def clear_screen():
    """Clear console screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu(task_count: int, completed_count: int):
    """
    Display main menu.
    
    Args:
        task_count: Total number of tasks
        completed_count: Number of completed tasks
    """
    clear_screen()
    print("┌─────────────────────────────────┐")
    print("│     TODO MANAGER v1.0           │")
    print("└─────────────────────────────────┘")
    print()
    print(f"Tasks: {task_count} total, {completed_count} completed")
    print()
    print("=== MENU ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print()


def get_menu_choice() -> int:
    """
    Get and validate menu choice.
    
    Returns:
        Valid menu choice (1-6)
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("❌ Invalid choice. Please enter 1-6.")
        except ValueError:
            print("❌ Please enter a valid number.")


def display_tasks(tasks: List[Dict[str, Any]]):
    """
    Display formatted task list.
    
    Args:
        tasks: List of task dictionaries
    """
    if not tasks:
        print("\nNo tasks yet. Add your first task!")
        return
    
    print("\nYour Tasks:")
    for task in tasks:
        status = "[✓]" if task["completed"] else "[ ]"
        # Format timestamp: YYYY-MM-DD HH:MM
        timestamp = task["created_at"][:16].replace("T", " ")
        print(f"  {task['id']}. {status} {task['title']} (Created: {timestamp})")


def get_task_input() -> str:
    """
    Get task title from user.
    
    Returns:
        Task title string
    """
    return input("\nEnter task title: ")


def get_task_id() -> int:
    """
    Get task ID from user.
    
    Returns:
        Task ID or -1 if invalid input
    """
    try:
        return int(input("\nEnter task ID: "))
    except ValueError:
        print("❌ Please enter a valid task number.")
        return -1


def confirm_action(prompt: str) -> bool:
    """
    Get y/n confirmation from user.
    
    Args:
        prompt: Confirmation question
        
    Returns:
        True if confirmed (y), False otherwise
    """
    response = input(f"\n{prompt} (y/n): ").lower().strip()
    return response == 'y'


def show_success(message: str):
    """
    Display success message.
    
    Args:
        message: Success message text
    """
    print(f"\n✓ {message}")


def show_error(message: str):
    """
    Display error message.
    
    Args:
        message: Error message text
    """
    print(f"\n❌ Error: {message}")


def pause():
    """Pause and wait for user to press Enter."""
    input("\nPress Enter to continue...")


def run_menu_loop(manager: TodoManager):
    """
    Main interactive menu loop.
    
    Args:
        manager: TodoManager instance for business logic
    """
    while True:
        # Display menu
        task_count = manager.get_task_count()
        completed_count = manager.get_completed_count()
        display_menu(task_count, completed_count)
        
        # Get choice
        choice = get_menu_choice()
        
        # Handle choice
        if choice == 1:
            handle_add_task(manager)
        elif choice == 2:
            handle_view_tasks(manager)
        elif choice == 3:
            handle_update_task(manager)
        elif choice == 4:
            handle_delete_task(manager)
        elif choice == 5:
            handle_toggle_complete(manager)
        elif choice == 6:
            handle_exit()
            break


def handle_add_task(manager: TodoManager):
    """Handle add task operation."""
    title = get_task_input()
    try:
        task = manager.add_task(title)
        show_success(f"Task added with ID: {task['id']}")
    except ValueError as e:
        show_error(str(e))
    pause()


def handle_view_tasks(manager: TodoManager):
    """Handle view tasks operation."""
    tasks = manager.get_all_tasks()
    display_tasks(tasks)
    pause()


def handle_update_task(manager: TodoManager):
    """Handle update task operation."""
    task_id = get_task_id()
    if task_id == -1:
        pause()
        return
    
    title = get_task_input()
    try:
        if manager.update_task(task_id, title):
            show_success(f"Task {task_id} updated")
        else:
            show_error("Task not found")
    except ValueError as e:
        show_error(str(e))
    pause()


def handle_delete_task(manager: TodoManager):
    """Handle delete task operation."""
    task_id = get_task_id()
    if task_id == -1:
        pause()
        return
    
    if confirm_action("Are you sure?"):
        if manager.delete_task(task_id):
            show_success(f"Task {task_id} deleted")
        else:
            show_error("Task not found")
    else:
        show_error("Deletion cancelled")
    pause()


def handle_toggle_complete(manager: TodoManager):
    """Handle toggle complete operation."""
    task_id = get_task_id()
    if task_id == -1:
        pause()
        return
    
    if manager.toggle_complete(task_id):
        # Get updated task to show new status
        task = manager.get_task_by_id(task_id)
        status = "complete" if task["completed"] else "incomplete"
        show_success(f"Task {task_id} marked as {status}")
    else:
        show_error("Task not found")
    pause()


def handle_exit():
    """Handle exit operation."""
    clear_screen()
    print("Goodbye! Your tasks will not be saved.")
    print()