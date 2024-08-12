class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append({"task": task, "complete": False})
        else:
            print("Task cannot be empty.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks, start=1):
            status = "X" if task["complete"] else " "
            print(f"{i}. [{status}] {task['task']}")

    def mark_task_complete(self, task_number):
        pass

    def delete_task(self, task_number):
        try:
            index = task_number - 1
            if 0 <= index < len(self.tasks):
                del self.tasks[index]
            else:
                print("Invalid task number.")
        except Exception as e:
            print(f"An error occurred: {e}")

def display_menu():
    print(""""\nWelcome to the To-Do List App!
    \nMenu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit""")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == "1":
            task = input("Enter the task description: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            pass
        elif choice == "4":
            try:
                task_number = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("Quitting the application.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
