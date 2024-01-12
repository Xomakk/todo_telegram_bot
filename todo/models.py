from database import Database


class Todo:
    """Класс задачи."""

    def __init__(self, id, user_id, content, status=0):
        self.id = id
        self.user_id = user_id
        self.content = content
        self.status = status

        self.__db = Database()

    def update(self, new_message):
        """Обновление текста задачи."""

        self.__db.execute(
            f"""
                UPDATE tasks SET content = '{new_message}'
                WHERE id = {self.id}
            """
        )
        self.__db.commit()

    def change_status(self):
        """Изменение статуса выполнения задачи на противоположный."""

        if self.status == 0:
            self.status = 1
        else:
            self.status = 0

        self.__db.execute(
            f"""
                UPDATE tasks SET status = {self.status}
                WHERE id = {self.id}
            """
        )
        self.__db.commit()


class TodoList:
    """Класс списка задач."""

    def __init__(self, user_id):
        self.tasks = []
        self.user_id = user_id

        self.__db = Database()

        self.__init_list()

    def __init_list(self):
        """Добавление всех задач пользователя в список."""

        self.__query = self.__db.execute(
            f"SELECT * FROM tasks WHERE userId = '{str(self.user_id)}'"
        )

        raw_todos = self.__query.fetchall()
        for todo in raw_todos:
            id, user_id, content, status = todo
            self.tasks.append(Todo(id, user_id, content, status))

    def create_task(self, message):
        """Создание новой задачи."""

        self.__db.execute(
            f"""
                INSERT INTO tasks(userId, content)
                VALUES ('{self.user_id}', '{message}')
            """
        )
        self.__db.commit()

    def delete_task(self, task_id):
        """Удаление задачи с указанным id."""

        self.__db.execute(
            f"""
                DELETE FROM tasks WHERE id = {task_id}
            """
        )
        self.__db.commit()
        self.tasks = list(filter(lambda t: t.id != task_id, self.tasks))

    def get_task_by_id(self, task_id) -> Todo | None:
        """Получение объекта задачи по id."""

        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
