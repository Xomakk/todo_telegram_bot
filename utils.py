from telebot import TeleBot
from telebot.types import Message

from todo.controllers import add_task, get_task_list, update_task, get_task


def user_input_new_task(message: Message, bot: TeleBot):
    """Обработка ввода текста новой задачи."""

    add_task(
        user_id=message.from_user.id,
        task_message=message.text
    )
    text, keyboard = get_task_list(str(message.from_user.id))
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


def user_input_edit_task(message: Message, bot: TeleBot, task_id: int):
    """Обработка ввода нового текста при редактировании задачи."""

    update_task(
        user_id=message.from_user.id,
        task_id=task_id,
        new_message=message.text
    )
    text, keyboard = get_task(str(message.from_user.id), task_id)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


def edit_message_before_callback(bot, call, text, keyboard):
    """Редактирование последнего сообщения на переданные текст и клавиатуру."""

    chat_id, message_id = call.message.chat.id, call.message.id
    if text:
        bot.edit_message_text(text, chat_id, message_id)
    if keyboard:
        bot.edit_message_reply_markup(chat_id, message_id, reply_markup=keyboard)
    bot.answer_callback_query(call.id)
