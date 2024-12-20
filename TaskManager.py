class task():
    def __init__(self):
        self.id = 0
        self.task = ""
        self.status = "Pending..."

class FileDataInSequence():
    def __init__(self):
        self.data_sequence = []

UserTask = task()

TaskNumber = input("\nEnter the Task Number: ")
repeat = int(TaskNumber)
TaskDataFile = open("TaskDataFile.txt", "w")
for task in range(repeat):
    TaskDataFile = open("TaskDataFile.txt", "a+")
    UserTask.task = input(f"Task {UserTask.id + 1}: ")
    UserTask.id += 1
    TaskDataFile.write("\n" + str(UserTask.id) + "\t")
    TaskDataFile.write(UserTask.task + "\t")
    TaskDataFile.write(UserTask.status + "\t")