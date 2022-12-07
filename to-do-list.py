class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
    
    def unmark_complete(self):
        self.completed = False


class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        self.tasks.remove(task)
    
    def display(self):
        for task in self.tasks:
            print(f"Task: {task.description} | Completed: {task.completed}")

# creating the ToDoList
tdl = ToDoList()

# creating the tasks
task_001 = Task("Create a program that manages a 'to-do-list'.")
task_002 = Task("Fly to the moon.")

# adding the tasks to the to-do-list
tdl.add_task(task_001)
tdl.add_task(task_002)

# display the to-do-list
tdl.display()

# remove a task
tdl.remove_task(task_002)
tdl.display()

# mark a task as completed
task_001.mark_complete()
tdl.display()