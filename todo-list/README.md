# ✅ To-Do List

A simple yet fully functional Python CLI to-do list manager. Keep track of your tasks during a session by adding, viewing, and removing them through an interactive menu.

## Features

- ➕ Add tasks with descriptions
- 📋 View all current tasks in a numbered list
- 🗑️ Remove tasks by their number
- ✅ Validation for empty input and out-of-range selections
- 🔄 Persistent in-memory session (tasks live until you exit)

## How to Run

```bash
python main.py
```

### Example Session

```
📋 To-Do List Manager
-------------------------
1. Add task
2. View tasks
3. Remove task
4. Exit

Enter your choice (1-4): 1
Enter task description: Buy groceries
✅ Task 'Buy groceries' added successfully.

Enter your choice (1-4): 2

Your tasks:
  1. Buy groceries

Enter your choice (1-4): 4

Goodbye! Stay productive. 👋
```

## Requirements

- Python 3.6+
- No external dependencies

## Project Structure

```
todo-list/
└── main.py   # Main script
```
