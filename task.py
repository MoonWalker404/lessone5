class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "Не выполнено"

    def mark_as_completed(self):
        self.status = "Выполнено"

# Создадим список для хранения всех задач
task_list = []

# Функция для добавления задачи
def add_task(description, deadline):
    new_task = Task(description, deadline)
    task_list.append(new_task)

# Функция для вывода списка текущих (не выполненных) задач
def print_current_tasks():
    for task in task_list:
        if task.status == "Не выполнено":
            print(f"Описание задачи: {task.description}, Срок выполнения: {task.deadline}, Статус: {task.status}")

# Пример использования:
add_task("Погулять с собакой", "30.09.2022")
add_task("Подготовить презентацию", "15.10.2022")
task_list[0].mark_as_completed()

print("Текущие задачи:")
print_current_tasks()