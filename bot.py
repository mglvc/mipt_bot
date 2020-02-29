import telebot
from telebot import types

TOKEN = ''

string = ''

bac, mag, phis, prmath, russ, inf = 0, 0, 0, 0, 0, 0

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Бакалавриат или специалитет', callback_data= 3))
    markup.add(telebot.types.InlineKeyboardButton(text='Магистратуру', callback_data= 4))
    #markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    bot.send_message(message.chat.id, text="Вы хотите поступить в...", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global bac, mag, phis, prmath, russ, inf
    if call.data == '3':

        bac = 1
        keyboardmain = types.InlineKeyboardMarkup(row_width=6)   
        keyboardmain.add(types.InlineKeyboardButton(text="куда вы можете поступить?", callback_data='exams'))
        keyboardmain.add(types.InlineKeyboardButton(text="олимпиады", callback_data='olimp'))
        keyboardmain.add(types.InlineKeyboardButton(text="целевое", callback_data="celevoe")) 
        keyboardmain.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data= 5))
        keyboardmain.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="вы собираетесь в бакалавриат или специалитет",reply_markup=keyboardmain)

    elif call.data == "celevoe":
    	keyboardmain = types.InlineKeyboardMarkup(row_width=1) 
    	keyboardmain.add(types.InlineKeyboardButton(text="back", callback_data="bacmenu"))
    	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="прием на целевое направление https://pk.mipt.ru/bachelor/corp/",reply_markup=keyboardmain)    	

    elif call.data == "exams":
    	phis, prmath, russ, inf = 0, 0, 0, 0
    	key = telebot.types.InlineKeyboardMarkup(row_width=4)
    	key.add(types.InlineKeyboardButton(text="физику, проф. математику и русский", callback_data="fmr"))
    	key.add(types.InlineKeyboardButton(text="физику, информатику, проф. математику и русский", callback_data="fimr"))
    	key.add(types.InlineKeyboardButton(text="информатику, проф. математику, русский", callback_data="mir"))
    	key.add(telebot.types.InlineKeyboardButton(text='back', callback_data="bacmenu"))
    	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Вы сдавали...",reply_markup=key)

    elif call.data == "olimp":
    	k = types.InlineKeyboardMarkup(row_width=1)
    	k.add(telebot.types.InlineKeyboardButton(text='back', callback_data="bacmenu"))
    	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Вы  можете поступить с помощью олимпиад из этого списка",reply_markup=k)
    
    elif call.data == "bacmenu":
    	keyboardmain = types.InlineKeyboardMarkup(row_width=5)    
    	keyboardmain.add(types.InlineKeyboardButton(text="куда вы можете поступить?", callback_data='exams'))
    	keyboardmain.add(types.InlineKeyboardButton(text="олимпиады", callback_data='olimp'))
    	keyboardmain.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data= 5))
    	keyboardmain.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
    	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="вы собираетесь в бакалавриат или специалитет",reply_markup=keyboardmain)

    elif call.data == 'fmr':
    	phis, prmath, russ = 1, 1, 1	
    	k = types.InlineKeyboardMarkup(row_width=1)
    	k.add(telebot.types.InlineKeyboardButton(text='back', callback_data="exams"))
    	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="физику, профильную математику, русский",reply_markup=k)
    	
    elif call.data == 'fimr':
    	phis, inf, prmath, russ = 1, 1, 1, 1
    	k = types.InlineKeyboardMarkup(row_width=1)
    	k.add(telebot.types.InlineKeyboardButton(text='back', callback_data="exams"))
    	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="физику, профильную математику, русскийи и информатику",reply_markup=k)
    
    elif call.data == 'mir':
    	inf, prmath, russ = 1, 1, 1
    	k = types.InlineKeyboardMarkup(row_width=1)
    	k.add(telebot.types.InlineKeyboardButton(text='back', callback_data="exams"))
    	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="информатику, профильную математику, русский",reply_markup=k)

    elif call.data == '4':
        answer = 'магистратуру'
        mag = 1
        key = types.InlineKeyboardMarkup(row_width=2)
        key.add(types.InlineKeyboardButton(text="почитать FAQ", callback_data="6"))
        key.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
        bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text= "вы собираетесь поступать в магистратуру", reply_markup=key)
    
    elif call.data == '6':
    	kay = types.InlineKeyboardMarkup(row_width = 2)
    	kay.add(types.InlineKeyboardButton(text="моего вопроса нет в FAQ, задать вопрос", callback_data="quest_mag"))
    	kay.add(types.InlineKeyboardButton(text="back", callback_data="mainmenu"))
    	bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text="вы можете прочитать FAQ перейдя по этой ссылке https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fmaster%2Fquestion-answer%2F&rhash=a6c88d20ddb864", reply_markup=kay)
    	
    elif call.data == '5':
    	key = types.InlineKeyboardMarkup(row_width = 2)
    	key.add(types.InlineKeyboardButton(text="моего вопроса нет в FAQ, задать вопрос", callback_data="quest_bac"))
    	key.add(types.InlineKeyboardButton(text="back", callback_data="bacmenu"))
    	bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text="вы можете прочитать FAQ перейдя по этой ссылке https://t.me/iv?url=https%3A%2F%2Fpk.mipt.ru%2Fbachelor%2Fquestion-answer%2F&rhash=a6c88d20ddb864", reply_markup=key)
    
    elif call.data == "quest_bac":
    	k = types.InlineKeyboardMarkup(row_width = 1)
    	k.add(types.InlineKeyboardButton(text='back', callback_data='bacmenu'))
    	bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text="напишите ваш вопрос", reply_markup=k)

    elif call.data == "quest_mag":
    	k = types.InlineKeyboardMarkup(row_width = 1)
    	k.add(types.InlineKeyboardButton(text='back', callback_data='4'))
    	bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text="напишите ваш вопрос", reply_markup=k)	

    elif call.data == 'mainmenu':
    	bac, mag = 0, 0
    	markup = telebot.types.InlineKeyboardMarkup()
    	markup.add(telebot.types.InlineKeyboardButton(text='Бакалавриат или специалитет', callback_data=3))
    	markup.add(telebot.types.InlineKeyboardButton(text='Магистратуру', callback_data=4))
    #markup.add(telebot.types.InlineKeyboardButton(text='Почитать FAQ', callback_data=5))
    	bot.send_message(call.message.chat.id, text="Вы хотите поступить в...",  reply_markup=markup)

@bot.message_handler(commands=['faq'])
def send_faq(message):
	keyboard = types.InlineKeyboardMarkup()
	url_button = types.InlineKeyboardButton(text="Перейти на FAQ", url="https://pk.mipt.ru/bachelor/question-answer/")
	keyboard.add(url_button)
	bot.send_message(message.chat.id, "Нажми на кнопку", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_ms(message):
	    global string
	    string = message.text.lower()
	    #print(string)

bot.polling()
