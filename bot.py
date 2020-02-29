import telebot
from telebot import types

TOKEN = '955620028:AAFuqC8MSVkQa-50OdCnCxNyI5BJXHCAf8c'

bac, mag, phis, prmath, russ, inf = 0, 0, 0, 0, 0, 0

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Бакалавриат или специалитет', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Магистратуру', callback_data=4))
    #markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    bot.send_message(message.chat.id, text="Вы хотите поступить в...", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global bac, mag, phis, prmath, russ, inf
    if call.data == '3':
        answer = 'бакалавриат или специалитет'
        bac = 1
        
        keyboardmain = types.InlineKeyboardMarkup(row_width=5)
        keyboardmain.add(types.InlineKeyboardButton(text="физику, проф. математику и русский", callback_data="11"))
        keyboardmain.add(types.InlineKeyboardButton(text="физику, информатику, проф. математику и русский", callback_data="12"))
        keyboardmain.add(types.InlineKeyboardButton(text="информатику, проф. математику, русский", callback_data="13"))
        keyboardmain.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
        #backbutton = types.InlineKeyboardButton(text="back", callback_data="mainmenu")
        keyboardmain.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="вы собираетесь в бакалавриат или специалитет. Вы сдавали...",reply_markup=keyboardmain)

    elif call.data == '11':
    	phis, prmath, russ = 1, 1, 1
    	bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    	bot.send_message(call.message.chat.id, "физику, профильную математику, русский")
    	
    elif call.data == '12':
    	phis, inf, prmath, russ = 1, 1, 1, 1
    	bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    	bot.send_message(call.message.chat.id, "физику, профильную математику, информатику, русский")
    
    elif call.data == '13':
    	inf, prmath, russ = 1, 1, 1
    	bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    	bot.send_message(call.message.chat.id, "информатику, профильную математику, русский")

    elif call.data == '4':
        answer = 'магистратуру'
        mag = 1
        key = types.InlineKeyboardMarkup(row_width=2)
        key.add(types.InlineKeyboardButton(text="FAQ", callback_data="6"))
        key.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
        bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text= "вы собираетесь поступать в магистратуру", reply_markup=key)
    
    elif call.data == '6':
    	k = types.InlineKeyboardMarkup(row_width = 1)
    	k.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
    	bot.send_message(call.message.chat.id, "вы можете прочитать FAQ перейдя по этой ссылке https://pk.mipt.ru/master/question-answer/")
    	
    elif call.data == '5':
    	k = types.InlineKeyboardMarkup(row_width = 1)
    	k.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
    	bot.send_message(call.message.chat.id, "вы можете прочитать FAQ перейдя по этой ссылке https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2Fquestion-answer%2F&rhash=a6c88d20ddb864")
    #bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id
    elif call.data == 'mainmenu':
    	markup = telebot.types.InlineKeyboardMarkup()
    	markup.add(telebot.types.InlineKeyboardButton(text='Бакалавриат или специалитет', callback_data=3))
    	markup.add(telebot.types.InlineKeyboardButton(text='Магистратуру', callback_data=4))
    #markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    	bot.send_message(call.message.chat.id, text="Вы хотите поступить в...", reply_markup=markup)

@bot.message_handler(commands=['faq'])
def send_faq(message):
	keyboard = types.InlineKeyboardMarkup()
	url_button = types.InlineKeyboardButton(text="Перейти на FAQ", url="https://pk.mipt.ru/bachelor/question-answer/")
	keyboard.add(url_button)
	bot.send_message(message.chat.id, "Нажми на кнопку", reply_markup=keyboard)

bot.polling()
