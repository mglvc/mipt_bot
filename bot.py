import csv
import re

import telebot
from telebot import types

from config.bot_config import TOKEN
from data.consts import BACH, MAST
from data.consts import QUEST_STATE, EXAMS_STATE
from data.buttons import *

import get_fac_info as gfi

# TOKEN = '955620028:AAFuqC8MSVkQa-50OdCnCxNyI5BJXHCAf8c'

string = ''

bot = telebot.TeleBot(TOKEN)

def cel(call):
    keyboardmain = types.InlineKeyboardMarkup(row_width=1)
    keyboardmain.add(
        types.InlineKeyboardButton(text="Назад", callback_data="bacmenu"))
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="Прием на целевое направление https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2Fcorp%2F&rhash=d8d1e26f87c4db",
                          reply_markup=keyboardmain)

def send_descr(call, data):
    chat_id = call.message.chat.id
    out =   f"{data['name']}\n" \
             "--------------\n" \
            f"{data['description']}\n" \
             "--------------\n" \
            f"{', '.join(data['address'])}\n" \
            f"{', '.join(data['phones'])}\n" \
            f"Email: {data['email']}\n" \
            f"Сайт:  {data['site']}"

    print(out)

    bot.send_message(chat_id, out)
    bachelor(call)
    return BACH

def bachelor(call):
    bac = 1
    keyboardmain = types.InlineKeyboardMarkup(row_width=6)
    keyboardmain.add(
        types.InlineKeyboardButton(text="Куда можно поступить?",
                                   callback_data='exams'))
    keyboardmain.add(
        types.InlineKeyboardButton(text="Описания факультетов",
                                   callback_data='facs'))
    keyboardmain.add(
        types.InlineKeyboardButton(text="🏅 Олимпиады дающие льготы", callback_data='olimp'))
    keyboardmain.add(
        types.InlineKeyboardButton(text="Целевое обучение за счет компаний", callback_data="celevoe"))
    keyboardmain.add(telebot.types.InlineKeyboardButton(text='❓ Часто задаваемые вопросы',
                                                        callback_data=5))
    keyboardmain.add(
        types.InlineKeyboardButton(text="Назад", callback_data="mainmenu"))
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="Вас интересует  бакалавриат или специалитет?",
                          reply_markup=keyboardmain)

def facs_info(call):
    chat_id = call.message.chat.id;
    keyboardmain = types.InlineKeyboardMarkup(row_width=6)
    keyboardmain.add(
        types.InlineKeyboardButton(text="ФРКТ",
                                   callback_data='FRKT'))
    keyboardmain.add(
        types.InlineKeyboardButton(text="ФПМИ", callback_data='FPMI'))
    keyboardmain.add(
        types.InlineKeyboardButton(text="ЛФИ", callback_data="LFI"))
    keyboardmain.add(
        types.InlineKeyboardButton(text='ФЭФМ', callback_data="FEFM"))
    keyboardmain.add(
        types.InlineKeyboardButton(text="ФБМФ", callback_data="FBMF"))
    keyboardmain.add(
        types.InlineKeyboardButton(text="ИНБИКСТ", callback_data="INBICST"))
    keyboardmain.add(
        types.InlineKeyboardButton(text="ФАКТ", callback_data="FAKT"))

    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="Выберите факультет",
                          reply_markup=keyboardmain)


def exams_read(call):
    chat_id = call.message.chat.id
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
                          text="Вы  можете поступить с учетом результатов олимпиад из этого списка https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2F2020_olympiads%2F&rhash=d8d1e26f87c4db",
                          reply_markup=k)


def maga(call):
    key = types.InlineKeyboardMarkup(row_width=2)
    key.add(types.InlineKeyboardButton(text="❓ Часто задаваемые вопросы", callback_data="6"))
    key.add(types.InlineKeyboardButton(text="Назад", callback_data="mainmenu"))
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="Для поступающих в магистратуру может быть полезна следующая информация",
                          reply_markup=key)


def faqmag(call):
    key = types.InlineKeyboardMarkup(row_width=2)
    key.add(types.InlineKeyboardButton(
        text=ask_question,
        callback_data="quest_mag"))
    key.add(types.InlineKeyboardButton(text="Назад", callback_data="maga"))
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="Вы можете прочитать FAQ перейдя по этой ссылке https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fmaster%2Fquestion-answer%2F&rhash=a6c88d20ddb864",
                          reply_markup=key)


def faqbac(call):
    key = types.InlineKeyboardMarkup(row_width=2)
    key.add(types.InlineKeyboardButton(
        text=ask_question,
        callback_data="quest_bac"))
    key.add(types.InlineKeyboardButton(text="Назад", callback_data="bacmenu"))
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="Вы можете прочитать FAQ перейдя по этой ссылке https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2Fquestion-answer%2F&rhash=a6c88d20ddb864",
                          reply_markup=key)
    return QUEST_STATE


def mainm(call):
    bac, mag = 0, 0
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(text='🎓 Бакалавриат или специалитет',
                                           callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='🎓 Магистратура',
                                                  callback_data=4))
    # markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    bot.send_message(chat_id=call.message.chat.id,
                     text="Выберете интересующую вас академическую степень или"
                          " задайте вопрос:", reply_markup=markup)

def quest(call):
    k = types.InlineKeyboardMarkup(row_width=1)
    k.add(types.InlineKeyboardButton(text='Назад', callback_data='4'))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Напишите ваш вопрос:", reply_markup=k)


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
def start_message(message, error=0):
    if error:
        bot.send_message(message.chat.id, message.text)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton(text='🎓 Бакалавриат или специалитет',
                                           callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='🎓 Магистратура',
                                                  callback_data=4))
    # markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    bot.send_message(message.chat.id, text=
    "🤖 Вас приветствет чат бот приемной комииссии МФТИ.\n"
    "Выберите интересующую вас академическую степень.\n"
    "Так же вы можете задать интересующий вас вопрос боту.",
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

    elif call.data == 'exams':
        return exams_read(call)

    elif call.data == 'facs':
        facs_info(call)

    elif call.data == 'FPMI':
        data = gfi.get_info('ФПМИ')
        return send_descr(call, data)

    elif call.data == 'LFI':
        data = gfi.get_info('ЛФИ')
        return send_descr(call, data)

    elif call.data == 'FEFM':
        data = gfi.get_info('ФЭФМ')
        return send_descr(call, data)

    elif call.data == 'FRKT':
        data = gfi.get_info('ФРКТ')
        return send_descr(call, data)

    elif call.data == 'FBMF':
        data = gfi.get_info('ФБМФ')
        return send_descr(call, data)

    elif call.data == 'INBICST':
        data = gfi.get_info('ИНБИКСТ')
        return send_descr(call, data)

    elif call.data == 'FACT':
        data = gfi.get_info('ФАКТ')
        return send_descr(call, data)

    return 0

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
