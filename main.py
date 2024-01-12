from telebot import TeleBot
import constants
from todo.controllers import get_task_list, get_task, change_status, delete_task
from telebot.types import Message, CallbackQuery

from utils import user_input_new_task, edit_message_before_callback, user_input_edit_task

bot = TeleBot(constants.TOKEN)


@bot.message_handler(commands=["help"])
def handle_start_command(message: Message):
    """Обработка команды help."""

    bot.send_message(message.chat.id, constants.HELP_MESSAGE)


@bot.message_handler(commands=["start"])
def handle_start_command(message: Message):
    """Обработка команды start."""

    text, keyboard = get_task_list(str(message.from_user.id))
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda action: True)
def handle_user_btn_action(call: CallbackQuery):
    """Обработка событий по нажатию кнопок встроенной клавиатуры."""

    if 'task_list' in call.data:
        # событие получение списка задач
        text, keyboard = get_task_list(call.from_user.id)
        edit_message_before_callback(bot, call, text, keyboard)

    if 'add_task' in call.data:
        # событие добавление задачи
        bot.send_message(call.message.chat.id, 'Напишите текст задачи')
        bot.register_next_step_handler(
            call.message,
            callback=user_input_new_task,
            bot=bot
        )
        bot.answer_callback_query(call.id)

    if 'view_task' in call.data:
        # событие получение задачи
        _, task_id = call.data.split('/')
        text, keyboard = get_task(
            user_id=str(call.from_user.id),
            task_id=int(task_id)
        )
        edit_message_before_callback(bot, call, text, keyboard)

    if 'change_status' in call.data:
        # событие изменения статуса задачи
        _, task_id = call.data.split('/')
        text, keyboard = change_status(
            user_id=str(call.from_user.id),
            task_id=int(task_id)
        )
        edit_message_before_callback(bot, call, text, keyboard)

    if 'edit' in call.data:
        # событие изменения задачи
        _, task_id = call.data.split('/')
        bot.send_message(call.message.chat.id, 'Напишите новый текст задачи')
        bot.register_next_step_handler(
            call.message,
            callback=user_input_edit_task,
            bot=bot,
            task_id=int(task_id)
        )
        bot.answer_callback_query(call.id)

    if 'delete' in call.data:
        # событие удаления задачи
        _, task_id = call.data.split('/')
        text, keyboard = delete_task(
            user_id=str(call.from_user.id),
            task_id=int(task_id)
        )
        edit_message_before_callback(bot, call, text, keyboard)


bot.polling(interval=1, non_stop=True)
