import telebot
import pandas as pd
from telebot import types

import csv
import re

TOKEN = '955620028:AAFuqC8MSVkQa-50OdCnCxNyI5BJXHCAf8c'

string = ''

def cel(c):
    keyboardmain = types.InlineKeyboardMarkup(row_width=1) 
    keyboardmain.add(types.InlineKeyboardButton(text="back", callback_data="bacmenu"))
    bot.edit_message_text(chat_id=c,message_id=call.message.message_id, text="прием на целевое направление https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2Fcorp%2F&rhash=d8d1e26f87c4db",reply_markup=keyboardmain)        

def bachelor(c):
    bac = 1
    keyboardmain = types.InlineKeyboardMarkup(row_width=6)   
    keyboardmain.add(types.InlineKeyboardButton(text="Куда вы можете поступить?", callback_data='exams'))
    keyboardmain.add(types.InlineKeyboardButton(text="Oлимпиады", callback_data='olimp'))
    keyboardmain.add(types.InlineKeyboardButton(text="Целевое", callback_data="celevoe")) 
    keyboardmain.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data= 5))
    keyboardmain.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
    bot.edit_message_text(chat_id=c,message_id=call.message.message_id, text="вы собираетесь в бакалавриат или специалитет",reply_markup=keyboardmain)

def olymp(c):
    k = types.InlineKeyboardMarkup(row_width=1)
    k.add(telebot.types.InlineKeyboardButton(text='back', callback_data="bacmenu"))
    bot.edit_message_text(chat_id=c,message_id=call.message.message_id, text="Вы  можете поступить с помощью олимпиад из этого списка https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2F2020_olympiads%2F&rhash=d8d1e26f87c4db",reply_markup=k)
 
def maga(c):
    #answer = 'магистратуру'
    mag = 1
    key = types.InlineKeyboardMarkup(row_width=2)
    key.add(types.InlineKeyboardButton(text="Почитать FAQ", callback_data="6"))
    key.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
    bot.edit_message_text(chat_id = c, message_id=call.message.message_id, text= "Вы собираетесь поступать в магистратуру", reply_markup=key)   

def faqmag(c):
    answer = 'магистратуру'
        mag = 1
        key = types.InlineKeyboardMarkup(row_width=2)
        key.add(types.InlineKeyboardButton(text="Почитать FAQ", callback_data="6"))
        key.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
        bot.edit_message_text(chat_id = c, message_id=call.message.message_id, text= "Вы собираетесь поступать в магистратуру", reply_markup=key)

def faqmag(c):
    key = types.InlineKeyboardMarkup(row_width = 2)
    key.add(types.InlineKeyboardButton(text="Моего вопроса нет в FAQ, задать вопрос", callback_data="quest_bac"))
    key.add(types.InlineKeyboardButton(text="back", callback_data="bacmenu"))
    bot.edit_message_text(chat_id = c, message_id=call.message.message_id, text="Вы можете прочитать FAQ перейдя по этой ссылке https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2Fquestion-answer%2F&rhash=a6c88d20ddb864", reply_markup=key)
   
def mainm(c):
    bac, mag = 0, 0
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Бакалавриат или специалитет', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Магистратуру', callback_data=4))
    #markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    bot.send_message(chat_id = c, text="Вы хотите поступить в...",  reply_markup=markup)

def quest_b(c):
    k = types.InlineKeyboardMarkup(row_width = 1)
    k.add(types.InlineKeyboardButton(text='back', callback_data='bacmenu'))
    bot.edit_message_text(chat_id = c, message_id=call.message.message_id, text="Напишите ваш вопрос", reply_markup=k)

def quest_m(c):
    k = types.InlineKeyboardMarkup(row_width = 1)
    k.add(types.InlineKeyboardButton(text='back', callback_data='4'))
    bot.edit_message_text(chat_id = c, message_id=call.message.message_id, text="Напишите ваш вопрос", reply_markup=k)   


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


df = pd.DataFrame({
	"user_id" : [],
	"bac" :[],
	"mag" :[],
	"bio" :[],
	"phis" :[], 
	"inf" :[],
	"chem" :[],
	"russ" :[], 
	"prmath" :[]
	})

bac, mag, phis, prmath, russ, inf = 0, 0, 0, 0, 0, 0

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Бакалавриат или специалитет', callback_data= 3))
    markup.add(telebot.types.InlineKeyboardButton(text='Магистратуру', callback_data= 4))
    #markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    bot.send_message(message.chat.id, text="Вы хотите поступить в...?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):	
    global bac, mag, phis, prmath, russ, inf
    
    if call.data == '3':
        bachelor(call.message.chat.id)

    elif call.data == "celevoe":
    	cel(call.message.chat.id)
    #elif call.data == "exams":
    #	phis, prmath, russ, inf = 0, 0, 0, 0
    #	key = telebot.types.InlineKeyboardMarkup(row_width=4)
    #	key.add(types.InlineKeyboardButton(text="Физику, проф. математику и русский", callback_data="fmr"))
    #	key.add(types.InlineKeyboardButton(text="Физику, информатику, проф. математику и русский", callback_data="fimr"))
    #	key.add(types.InlineKeyboardButton(text="Информатику, проф. математику, русский", callback_data="mir"))
    #	key.add(telebot.types.InlineKeyboardButton(text='back', callback_data="bacmenu"))
    #	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Вы сдавали...",reply_markup=key)

    elif call.data == "olimp":
        olymp(call.message.chat.id)
    	
    elif call.data == "bacmenu":
    	bachelor(call.message.chat.id)

    #elif call.data == 'fmr':
    #	phis, prmath, russ = 1, 1, 1	
    #	k = types.InlineKeyboardMarkup(row_width=1)
    #	k.add(telebot.types.InlineKeyboardButton(text='back', callback_data="exams"))
    #	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Физику, профильную математику, русский",reply_markup=k)
    	
    #elif call.data == 'fimr':
    #	phis, inf, prmath, russ = 1, 1, 1, 1
    #	k = types.InlineKeyboardMarkup(row_width=1)
    #	k.add(telebot.types.InlineKeyboardButton(text='back', callback_data="exams"))
    #	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Физику, профильную математику, русскийи и информатику",reply_markup=k)
    
   # elif call.data == 'mir':
    #	inf, prmath, russ = 1, 1, 1
    #	k = types.InlineKeyboardMarkup(row_width=1)
    #	k.add(telebot.types.InlineKeyboardButton(text='back', callback_data="exams"))
    #	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Информатику, профильную математику, русский",reply_markup=k)

    elif call.data == '4':
        maga(call.message.chat.id)
    
    elif call.data == '6':
    	faqmag(call.message.chat.id)
    	
    elif call.data == '5':
    	faqbac(call.message.chat.id)

    elif call.data == "quest_bac":
    	quest_b(call.message.chat.id)

    elif call.data == "quest_mag":
    	quest_m(call.message.chat.id)

    elif call.data == 'mainmenu':
        mainm(call.message.chat.id)



@bot.message_handler(content_types=['text'])
def send_ms(message):
	global string
    string = message.text.lower()
    print(string)
    res = list(get_info(string))
    for i in range(0, len(res), 2):
        print(res[i])
    #bot.send_message(message.chat.id, res)
    #как красиво выводить?

bot.polling()
