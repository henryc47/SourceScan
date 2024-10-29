#Just some random code I got chatGPT to generate

# Simple CLI-based Todo List Manager

import sys

# Initialize an empty list to store tasks
todo_list = []

def show_menu():
    """Display the main menu options."""
    print("\n--- Todo List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    """Display the tasks in the todo list."""
    if not todo_list:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task to the todo list."""
    task = input("Enter a new task: ").strip()
    if task:
        todo_list.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Empty task not added.")

def remove_task():
    """Remove a task by its number."""
    try:
        view_tasks()
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the Todo List manager."""
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

# Run the Todo List manager
if __name__ == "__main__":
    main()

#foo
#foo
#foo
#foo
#foo
#foo
#foo
#foo
#foo
#foo
#foo
#foo