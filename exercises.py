# exercise 1
class Task:

    # instance method
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return "* Task: {}".format(self.description)

# exercise 2
class TodoList:

    # instance method
    def __init__(self, name):
        self.name = name
        self.tasks = []

    # instance method
    def add_task(self, task):
        self.tasks.append(task)

# create the tasks
task1 = Task("get groceries", "today")
task2 = Task("wash the car", "tomorrow")
task3 = Task("do laundry", "today")

# add them to the todo list
todo = TodoList("My Todo List")
print("Tasks in {}:".format(todo.name))
todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)

# check the tasks in the todo list
for task in todo.tasks:
    print(task)
