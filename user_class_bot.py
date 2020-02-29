# import db_connect
from send_message import *

# BD connect
# conn = db_connect.conn_to_db()


class UserBot:
    def __init__(self, bot, update, user):
        self.av_states = [0, 1, 2]  # 0 - start, 1 - base, 2- ask question
        self.state = self.av_states[0]
        self.user_id = user.id
        self.user_name = user.first_name
        self.telebot = bot
        # Check user in db
        # if self.find_user_db(user) == 0:
            # place for 1st question
            # pass
            # place for 2nd question
            # pass
        self.state = self.av_states[1]

    def find_user_db(self, user):
        with conn.cursor() as cur:
            cur.execute(f"SELECT * from users WHERE {user.id} = user_id")
            print(user.id)
            data = cur.fetchone()
            if data:
                self.degree_status = data[1]
                self.gov_status = data[2]
                return 1
            else:
                cur.execute(f"INSERT into users (user_id, name) "
                            f"values ({user.id}, '{user.username}')")
                return 0

    def update_data(self):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE users"
                        f"SET"
                        f"degree_status = {self.degree_status}"
                        f"gov_status = {self.gov_status}"
                        f"WHERE user_id = {self.user_id}")

    def handle_message(self, message):
        if self.state == 2:
            # Place for searching question algo
            pass
        else:
            send_help_message(self.telebot, message.chat.id)

    def handle_commands(self, message):
        print("Message from class", message.text[1:])
        if message.text[1:] in ['start', 'reset']:
            # self.telebot.send_message(message.chat.id, "Ololo")
            send_start_message(self.telebot, message.chat.id)
        elif message.text[1:] == 'faq':
            send_faq_message(self.telebot, message.chat.id)
        else:
            send_help_message(self.telebot, message.chat.id)
