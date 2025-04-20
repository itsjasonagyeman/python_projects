class Task:
    def __init__(self, name, priority="Low", status="Pending"):
        self.name = name
        self.priority = priority  # e.g. Low, Medium, High
        self.status = status      # e.g. Pending, Completed

    def __str__(self):
        return f"{self.name} | Priority: {self.priority} | Status: {self.status}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Removed task: {removed.name}")
        else:
            print("Invalid index.")

    def update_task(self, index, name=None, priority=None, status=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if name:
                task.name = name
            if priority:
                task.priority = priority
            if status:
                task.status = status
            print("Task updated!")
        else:
            print("Invalid index.")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.name}|{task.priority}|{task.status}\n")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    name, priority, status = line.strip().split("|")
                    self.tasks.append(Task(name, priority, status))
        except FileNotFoundError:
            print("No saved tasks found. Starting fresh.")
