import csv
import re

import telebot
from telebot import types

from config.bot_config import TOKEN
from data.consts import BACH, MAST
from data.consts import QUEST_STATE

# TOKEN = '955620028:AAFuqC8MSVkQa-50OdCnCxNyI5BJXHCAf8c'

string = ''

bot = telebot.TeleBot(TOKEN)

def cel(call):
    keyboardmain = types.InlineKeyboardMarkup(row_width=1)
    keyboardmain.add(
        types.InlineKeyboardButton(text="back", callback_data="bacmenu"))
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="прием на целевое направление https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2Fcorp%2F&rhash=d8d1e26f87c4db",
                          reply_markup=keyboardmain)


def bachelor(call):
    bac = 1
    keyboardmain = types.InlineKeyboardMarkup(row_width=6)
    keyboardmain.add(
        types.InlineKeyboardButton(text="Куда вы можете поступить?",
                                   callback_data='exams'))
    keyboardmain.add(
        types.InlineKeyboardButton(text="Oлимпиады", callback_data='olimp'))
    keyboardmain.add(
        types.InlineKeyboardButton(text="Целевое", callback_data="celevoe"))
    keyboardmain.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ',
                                                        callback_data=5))
    keyboardmain.add(
        types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="вы собираетесь в бакалавриат или специалитет",
                          reply_markup=keyboardmain)

def exams_read(call):
    chat_id = call.message.chat.id;
    bot.send_message(chat_id,
            "Введите экзамены точно в данном порядке:\n"
            "Математика Русский Биология Информатика Физика Химия\n"
            "-------------\n"
            "Те предметы, что не надо учитывать, заполняйте нулём.\n"
            "Пример: 92 88 0 100 76 0")
    return EXAMS_STATE


def olymp(call):
    k = types.InlineKeyboardMarkup(row_width=1)
    k.add(telebot.types.InlineKeyboardButton(text='back',
                                             callback_data="bacmenu"))
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="Вы  можете поступить с помощью олимпиад из этого списка https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2F2020_olympiads%2F&rhash=d8d1e26f87c4db",
                          reply_markup=k)


def maga(call):
    # answer = 'магистратуру'
    mag = 1
    key = types.InlineKeyboardMarkup(row_width=2)
    key.add(types.InlineKeyboardButton(text="Почитать FAQ", callback_data="6"))
    key.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
    bot.edit_message_text(chat_id=call.chat.id,
                          message_id=call.message.message_id,
                          text="Вы собираетесь поступать в магистратуру",
                          reply_markup=key)


def faqmag(call):
    answer = 'магистратуру'
    mag = 1
    key = types.InlineKeyboardMarkup(row_width=2)
    key.add(types.InlineKeyboardButton(text="Почитать FAQ", callback_data="6"))
    key.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
    bot.edit_message_text(chat_id=call, message_id=call.message.message_id,
                          text="Вы собираетесь поступать в магистратуру",
                          reply_markup=key)


def faqbac(call):
    key = types.InlineKeyboardMarkup(row_width=2)
    key.add(types.InlineKeyboardButton(
        text="Моего вопроса нет в FAQ, задать вопрос",
        callback_data="quest_bac"))
    key.add(types.InlineKeyboardButton(text="back", callback_data="bacmenu"))
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="Вы можете прочитать FAQ перейдя по этой ссылке https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2Fquestion-answer%2F&rhash=a6c88d20ddb864",
                          reply_markup=key)
    return QUEST_STATE


def mainm(call):
    bac, mag = 0, 0
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(text='Бакалавриат или специалитет',
                                           callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Магистратуру',
                                                  callback_data=4))
    # markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    bot.send_message(chat_id=call.message.chat.id,
                     text="Вы хотите поступить в...", reply_markup=markup)

def quest(call):
    k = types.InlineKeyboardMarkup(row_width=1)
    k.add(types.InlineKeyboardButton(text='back', callback_data='4'))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Напишите ваш вопрос", reply_markup=k)


def get_info(fac, csv_path):
    response = {
        "name": [],
        "description": [],
        "address": [],
        "phones": [],
        "email": [],
        "site": []
    }

    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            if not fac in row[0]:
                continue
            response = {
                "name": re.sub(r'\s+', ' ', row[0]),
                "description": re.sub(r'\s+', ' ', row[1]),
                "address": row[2].split('\n'),
                "phones": [row[3], row[4]],
                "email": row[5],
                "site": row[6]
            }
            break

    return response

bac, mag, phis, prmath, russ, inf = 0, 0, 0, 0, 0, 0

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(text='Бакалавриат или специалитет',
                                           callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Магистратуру',
                                                  callback_data=4))
    # markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    bot.send_message(message.chat.id, text="Вы хотите поступить в...?",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global bac, mag, phis, prmath, russ, inf

    if call.data == '3':
        return bachelor(call)

    elif call.data == "celevoe":
        cel(call)

    elif call.data == "olimp":
        olymp(call)

    elif call.data == "bacmenu":
        bachelor(call)
        return BACH

    elif call.data == '4':
        maga(call)
        return MAST

    elif call.data == '6':
        faqmag(call)

    elif call.data == '5':
        return faqbac(call)

    elif call.data == "quest_bac":
        quest(call)
        return QUEST_STATE

    elif call.data == "quest_mag":
        quest(call)
        print("quest_state", QUEST_STATE)
        return QUEST_STATE

    elif call.data == 'mainmenu':
        mainm(call)
    return 0

    elif call.data == 'exams':
        return exams_read(call)

# @bot.message_handler(content_types=['text'])
# def send_ms(message):
# 	global string
#     string = message.text.lower()
#     print(string)
#     res = list(get_info(string))
#     for i in range(0, len(res), 2):
#         print(res[i])
#     #bot.send_message(message.chat.id, res)
#     #как красиво выводить?

# bot.polling()
