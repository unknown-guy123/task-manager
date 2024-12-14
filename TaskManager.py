
class task():
    def __init__(self):
        self.id = 0
        self.task = ""
        self.status = "Pending..."

UserTask = task()

TaskNumber = input("\nEnter the Task Number: ")
repeat = int(TaskNumber)

for task in range(repeat):
    UserTask.task = input(f"Task {UserTask.id + 1}: ")
    UserTask.id += 1