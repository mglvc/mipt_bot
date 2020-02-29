import telebot

import db_connect

update = telebot.types.Update
mes = telebot.types.Message()
user = telebot.types.User

conn = db_connect.conn_to_db()


class UserBot:
    def __init__(self, update, user):
        self.user_id = user.id
        self.user_name = user.first_name
        # Check user in db
        if self.find_user_db(user) == 0:
            # place for 1st question
            pass
            # place for 2nd question
            pass

    def find_user_db(self, user):
        with conn.cursor() as cur:
            cur.execute(f"SELECT * from users WHERE {user.id} = user_id")
            data = cur.fetchone()
            if data:
                self.degree_status = data[1]
                self.gov_status = data[2]
                return 1
            else:
                cur.execute(
                    f"INSERT into users (user_id, name)"
                    f"values({user.id}, {user.first_name}")
                return 0

    def update_data(self):
        with conn.cursor() as cur:
            cur.execute(f"UPDATE users"
                        f"SET"
                        f"degree_status = {self.degree_status}"
                        f"gov_status = {self.gov_status}"
                        f"WHERE user_id = {self.user_id}")


tmp_bot = UserBot(mes)
update.message.from_user
