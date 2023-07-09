Certainly! Here's an example of a simple to-do list application implemented in Python:

```python
tasks = []

def display_menu():
    print("TODO List")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def mark_completed():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['task']} - {'Completed' if task['completed'] else 'Not Completed'}")
    
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['task']} - {'Completed' if task['completed'] else 'Not Completed'}")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        mark_completed()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
```

This code provides a basic to-do list functionality where you can add tasks, mark tasks as completed, and view the tasks. It will continue running until you choose to exit by entering '4'.

Note that this implementation uses a list to store the tasks, where each task is a dictionary containing the task description and a boolean flag indicating whether it is completed or not.
