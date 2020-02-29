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
    markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    bot.send_message(message.chat.id, text="Вы хотите поступить в...", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global bac, mag, phis, prmath, russ, inf
    #bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    #answer = ''
    if call.data == '3':
        answer = 'бакалавриат или специалитет'
        bac = 1
        print(bac)
        bot.send_message(call.message.chat.id, answer)
    elif call.data == '4':
        answer = 'магистратуру'
        mag = 1
        bot.send_message(call.message.chat.id, answer)
    elif call.data == '5':
        bot.send_message(call.message.chat.id, "вы можете прочитать FAQ перейдя по этой ссылке https://pk.mipt.ru/bachelor/question-answer/")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


    	bot.send_message(message.chat.id, text="Вы сдавали...", reply_markup=markup)



@bot.message_handler(commands=['faq'])
def send_faq(message):
		keyboard = types.InlineKeyboardMarkup()
		url_button = types.InlineKeyboardButton(text="Перейти на FAQ", url="https://pk.mipt.ru/bachelor/question-answer/")
		keyboard.add(url_button)
		bot.send_message(message.chat.id, "Нажми на кнопку", reply_markup=keyboard)

#@bot.message_handler(content_types=['text'])
#def send_text(message):

bot.polling()
