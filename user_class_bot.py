import bot
import bot as message_handlers
import compare_old as compare
import db_connect
from calc_ege import calc_ege
from data.consts import delimiter
from data.consts import subjects_in_db_start, subjects_in_db_end
from send_message import *


# BD connect
conn = db_connect.conn_to_db()


class UserBot:
    def __init__(self, bot, update, user):
        self.av_states = [0, 1, 2]  # 0 - start, 1 - base, 2- ask question
        self.state = self.av_states[0]
        self.user_id = user.id
        self.user_name = user.first_name
        self.telebot = bot
        # Check user in db
        if self.find_user_db(user, update) == 0:
            # place for 1st question

            # place for 2nd question
            pass
        # self.state = self.av_states[1]

    def init_subjects(self, data):
        self.math = data[0]
        self.russian = data[1]
        self.biology = data[2]
        self.informatics = data[3]
        self.physics = data[4]
        self.chemistry = data[5]

    def find_user_db(self, user, update):
        print("Data", user, update)
        with conn.cursor() as cur:
            cur.execute(f"SELECT * from users WHERE {user.id} = user_id")
            # print(user.id)
            data = cur.fetchone()
            if data:
                print(f"User {user.id}, {user.first_name} already in DB")
                self.degree_status = data[2]
                self.gov_status = data[3]
                self.state = data[5]
                self.init_subjects(data[subjects_in_db_start:
                                        subjects_in_db_end])
                return 1
            else:
                cur.execute(
                    f"INSERT into users (user_id, name, last_update_id) "
                    f"values ({user.id}, '{user.username}', {update.update_id})")
                print(f"Added user {user.id}, {user.first_name} in DB")
                self.init_subjects([0 for _ in range(6)])
                conn.commit()
                return 0

    def update_data(self):
        with conn.cursor() as cur:
            print(self.degree_status, self.gov_status, self.state, self.user_id)
            cur.execute(f"UPDATE users "
                        f"SET "
                        f"degree_status = {self.degree_status}, "
                        f"gov_status = {self.gov_status}, "
                        f"state = {self.state}, "
                        f"math = {self.math}, "
                        f"russian = {self.russian}, "
                        f"biology = {self.biology}, "
                        f"informatics = {self.informatics}, "
                        f"physics = {self.physics}, "
                        f"chemistry = {self.chemistry} "
                        f"WHERE user_id = {self.user_id} ")

            conn.commit()

    def handle_message(self, message):
        if self.state == bot.EXAMS_STATE:
            result = message.text.split()
            if len(result) < 6:
                self.state = 0
                self.update_data()
                message.text = "Мало данных"
                return bot.start_message(message, -1)
            self.init_subjects([int(sub) for sub in result])
            exams = {
                "math": self.math,
                "russ": self.russian,
                "bio": self.biology,
                "info": self.informatics,
                "phys": self.physics,
                "chem": self.chemistry
            }
            opps = calc_ege(exams)
            if not len(opps):
                self.state = 0
                self.update_data()
                message.text = "Не нашлось факультета под ваши данные"
                return bot.start_message(message, -1)
            out = '\n\n===========\n\n'.join([' '.join(row) for row in opps])
            self.telebot.send_message(message.chat.id, out)
            self.state = 0
            self.update_data()
            return bot.start_message(message)

        else:
            result = compare.compare(message.text)
            if isinstance(result, str):
                self.telebot.send_message(message.chat.id, result)
            else:
                mes = ""
                for i, ans in enumerate(result):
                    mes += ans[0] + '\n' + ans[1]
                    if i != len(result) - 1:
                        mes += delimiter
                self.telebot.send_message(message.chat.id, mes)

    def handle_commands(self, message):
        print("Message from class", message.text[1:])
        if message.text[1:] in ['start', 'reset']:
            message_handlers.start_message(message)
            # send_start_message(self.telebot, message.chat.id)
        elif message.text[1:] == 'faq':
            send_faq_message(self.telebot, message.chat.id)
        else:
            send_help_message(self.telebot, message.chat.id)

    def handle_query(self, call):
        t = bot.query_handler(call)
        if t in [bot.BACH, bot.MAST]:
            self.degree_status = t
        elif t:
            self.state = t
        print(self.state, call.data)
        self.update_data()
