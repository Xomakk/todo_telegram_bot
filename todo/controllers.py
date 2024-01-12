from todo.models import TodoList
from todo.views import todo_list_view, task_view


def add_task(user_id, task_message):
    """Обработка добавления новой задачи."""

    todo_list = TodoList(user_id)
    todo_list.create_task(task_message)


def change_status(user_id, task_id):
    """Обработка изменения статуса задачи."""

    todo_list = TodoList(user_id)
    task = todo_list.get_task_by_id(task_id)
    task.change_status()
    return task_view(task)


def update_task(user_id, task_id, new_message):
    """Обработка изменения текста задачи."""

    todo_list = TodoList(user_id)
    task = todo_list.get_task_by_id(task_id)
    task.update(new_message)
    return task_view(task)


def delete_task(user_id, task_id):
    """Обработка удаления задачи."""

    todo_list = TodoList(user_id)
    todo_list.delete_task(task_id)
    return todo_list_view(todo_list)


def get_task(user_id, task_id):
    """Обработка получения и представления задачи с указанным id."""

    todo_list = TodoList(user_id)
    task = todo_list.get_task_by_id(task_id)
    return task_view(task)


def get_task_list(user_id):
    """Обработка получения и представления всех задач пользователя, чей id был передан."""

    todo_list = TodoList(user_id)
    return todo_list_view(todo_list)
