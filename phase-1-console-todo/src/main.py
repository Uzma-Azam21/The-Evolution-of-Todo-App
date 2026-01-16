"""
Console Todo Application - Entry Point

Phase I: In-memory Python console todo app
Interactive menu-driven interface for task management
"""

from todo_manager import TodoManager
from ui import run_menu_loop


def main():
    """Launch the todo application."""
    try:
        # Initialize todo manager
        manager = TodoManager()
        
        # Start interactive menu loop
        run_menu_loop(manager)
        
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nGoodbye! Your tasks will not be saved.")
    except Exception as e:
        # Catch any unexpected errors
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please report this issue.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())