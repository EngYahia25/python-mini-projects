"""
To-Do List
----------
A simple interactive CLI to-do list manager. Users can add,
view, and remove tasks during a session.
"""


def display_menu():
    """Print the main menu options."""
    print("\n📋 To-Do List Manager")
    print("-" * 25)
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")


def add_task(tasks: list):
    """Prompt the user for a task name and add it to the list."""
    task = input("Enter task description: ").strip()
    if not task:
        print("Task description cannot be empty.")
        return
    tasks.append(task)
    print(f"✅ Task '{task}' added successfully.")


def view_tasks(tasks: list):
    """Display all current tasks or notify the user if none exist."""
    if not tasks:
        print("📭 No tasks yet. Add one!")
        return
    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"  {index}. {task}")


def remove_task(tasks: list):
    """Prompt the user to select a task by number and remove it."""
    if not tasks:
        print("📭 No tasks to remove.")
        return

    view_tasks(tasks)

    while True:
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            task_index = task_number - 1
            if 0 <= task_index < len(tasks):
                removed = tasks.pop(task_index)
                print(f"🗑️  Task '{removed}' removed successfully.")
                return
            print(f"Please enter a number between 1 and {len(tasks)}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    """Main entry point for the To-Do List manager."""
    tasks = []

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("\nGoodbye! Stay productive. 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
