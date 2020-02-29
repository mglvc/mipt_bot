from data import messages


def send_help_message(bot, chat_id):
    bot.send_message(chat_id, text=messages.help)

def send_start_message(bot, chat_id):
    # Keyboard if needed
    print("message from fuc!")
    bot.send_message(chat_id, text=messages.start)

def send_faq_message(bot, chat_id):
    # Keyboard if needed
    bot.send_message(chat_id, text=messages.faq)