from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def todo_list_view(todo_list):
    kb = InlineKeyboardMarkup()

    # отображение кнопок для перехода на задачу
    for index, task in enumerate(todo_list.tasks):
        btn_task = InlineKeyboardButton(
            text=f'{index + 1}. {task.content}',
            callback_data=f'view_task/{task.id}'
        )
        kb.row(btn_task)

    # кпнока создания новой задачи
    btn_add_task = InlineKeyboardButton(
        text='Добавить новую',
        callback_data='add_task'
    )
    kb.row(btn_add_task)

    # сообщение-заголовок
    message_content = 'Ваш список задач:'
    return message_content, kb


def task_view(task):
    kb = InlineKeyboardMarkup()

    btn_chande_status = InlineKeyboardButton(
        text='Поставить "ВЫПОЛНЕНО"' if task.status == 0 else 'Поставить "НЕ ВЫПОЛНЕНО"',
        callback_data=f'change_status/{task.id}'
    )
    btn_edit = InlineKeyboardButton(
        text='Изменить',
        callback_data=f'edit/{task.id}'
    )
    btn_delete = InlineKeyboardButton(
        text='Удалить',
        callback_data=f'delete/{task.id}'
    )
    btn_list_view = InlineKeyboardButton(
        text='<- Назад',
        callback_data='task_list'
    )

    kb.add(btn_chande_status, btn_edit, btn_delete, btn_list_view, row_width=1)

    # сообщение-заголовок
    message_content = f'{task.content}\n\nСтатус: {"ВЫПОЛНЕНО" if task.status == 1 else "НЕ ВЫПОЛНЕНО"}'
    return message_content, kb
