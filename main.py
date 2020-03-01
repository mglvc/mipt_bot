import json
import logging

import telebot

import bot as messages_handler
# import compare
from config.aws_config import AWS_URL
from config.bot_config import TOKEN
from data import messages
# import db_connect
from user_class_bot import UserBot

# from handlers.keyboard_constructors import create_keyboard, add_back_button
# from my_config import config

# conn = db_connect.conn_to_db()

# Initializing bot and logging
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(TOKEN)

# Resetting WebHook
bot.remove_webhook()
bot.set_webhook(url=AWS_URL)

# Const data
http_success = {'statusCode': 200}
http_error = {'statusCode': 403}

# Setting up Bot info
updates_list = list()


def lambda_handler(event, context):
    try:
        request = json.loads(event['body'])
    except Exception:
        return http_error
    update = telebot.types.Update.de_json(json.dumps(request))
    print(update)

    if update.update_id not in updates_list:
        updates_list.append(update.update_id)
    else:
        return http_success

    if update.message:
        handle_message(update)
    elif update.callback_query:
        handle_query(update, update.callback_query)
        # messages_handler.query_handler()
    else:
        bot.send_message(update.chat.id, messages.help)
    return http_success


def handle_message(update):
    message = update.message
    user_bot = UserBot(bot, update, update.message.from_user)
    print(user_bot.user_id, user_bot.user_name)
    if message.content_type == 'text' and message.text[0] == '/':
        user_bot.handle_commands(message)
    elif message.content_type == 'sticker':
        bot.reply_to(message, message.sticker.emoji)
    else:
        user_bot.handle_message(message)
        # result = compare.compare(update.message.text)
        # if isinstance(result, str):
        #     bot.send_message(update.message.chat.id, result)
        # else:
        #     mes = ""
        #     for i, ans in enumerate(result):
        #         mes += ans[0] + '\n' + ans[1]
        #         if i != len(result) - 1:
        #             mes += delimiter
        #     bot.send_message(update.message.chat.id, mes)
        pass

def handle_query(update, call):
    user_bot = UserBot(bot, update, update.callback_query.from_user)
    user_bot.handle_query(call)
#     data = query.data
#     chat_id = query.message.chat.id
#     keyboard = None
#     message = "Ooops! Is it error???"
#     if data == 'projects':
#         keyboard = create_keyboard(btn_type='url', **buttons.project_buttons)
#         message = messages.projects
#     elif data == 'education':
#         message = messages.education
#     elif data == 'links':
#         keyboard = create_keyboard(btn_type='url', **buttons.link_buttons)
#         message = messages.links
#     elif data == 'back':
#         keyboard = create_keyboard(**buttons.start_buttons)
#         message = messages.greetings
#     elif data == 'experience':
#         message = messages.experience
#     elif data == 'contacts':
#         message = messages.contacts
#     if data != 'back':
#         keyboard = add_back_button(keyboard)
#     bot.send_message(chat_id, message, reply_markup=keyboard)


# def handle_command(message):
#     command = message.text[1:]
#     if command == 'start':
#         post_start_message(message.chat.id)
#     elif command == 'reset':
#         post_start_message(message.chat.id)
#     else:
#         bot.send_message(message.chat.id, messages.help)
