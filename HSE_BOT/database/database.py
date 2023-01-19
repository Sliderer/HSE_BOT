import sqlite3
from models import Deadline, User
from typing import List
from models import DateTime
from logger import Logger


class Database:
    connection_string = 'HSE_bot.db'

    def __init__(self):
        pass

    def __execute_command(self, command: str):
        result = None
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            result = cursor.fetchall()
        return result

    def add_deadline(self, deadline: Deadline):
        user_id = deadline.user_id
        title = deadline.title
        description = deadline.description
        date = deadline.date
        time = deadline.time

        command = f"INSERT INTO deadlines VALUES (NULL, {user_id}, '{title}', '{description}', '{date}', '{time}')" \
                  f" RETURNING *"
        result = self.__execute_command(command)
        return result

    def is_user_exists(self, user_id: int) -> bool:
        command = f'SELECT * FROM users WHERE user_id={user_id}'
        result = self.__execute_command(command)
        return len(result) != 0

    def find_user(self, user: User) -> List[User]:
        command = f'SELECT * FROM users WHERE user_id={user.user_id}'
        result = self.__execute_command(command)
        return result

    def add_user(self, user: User):
        if not self.is_user_exists(user.user_id):
            command = f"INSERT INTO users VALUES ({user.user_id}, '{user.first_name}', '{user.second_name}')"
            self.__execute_command(command)

    def __insert_daily_deadline(self, deadline_id:int, deadline: Deadline):
        command = f"INSERT INTO daily_deadlines VALUES ({deadline_id}, '{deadline.user_id}', '{deadline.title}', " \
                  f"'{deadline.description}', '{deadline.date}', '{deadline.time}')"
        self.__execute_command(command)

    def __insert_daily_deadline_part(self, deadline_id: int, deadline: Deadline):
        command = f"INSERT INTO daily_deadlines_part VALUES ({deadline_id}, '{deadline.user_id}', '{deadline.title}', " \
                  f"'{deadline.description}', '{deadline.date}', '{deadline.time}')"
        self.__execute_command(command)

    def __truncate_table(self, table_name: str):
        command = f'DELETE FROM {table_name}'
        self.__execute_command(command)

    def update_daily_deadlines(self, date_time: DateTime):
        date = date_time.date
        self.__truncate_table('daily_deadlines')
        command = f"SELECT * FROM deadlines WHERE date='{date}'"
        daily_deadlines = self.__execute_command(command)
        for deadline in daily_deadlines:

            data = {
                    'title': deadline[2],
                    'description': deadline[3],
                    'date': deadline[4],
                    'time': deadline[5]
                    }

            current_deadline = Deadline(user_id=deadline[1], data=data)
            self.__insert_daily_deadline(deadline[0], current_deadline)

        Logger.info('daily deadlines updated')

    def add_deadline_to_daily_deadlines(self, deadline_id: int, deadline: Deadline):
        command = f"INSERT INTO daily_deadlines VALUES ({deadline_id}, '{deadline.user_id}', '{deadline.title}', " \
                  f"'{deadline.description}', '{deadline.date}', '{deadline.time}')"
        self.__execute_command(command)

    def add_deadline_to_daily_deadlines_part(self, deadline_id: int, deadline: Deadline):
        command = f"INSERT INTO daily_deadlines_part VALUES ({deadline_id}, '{deadline.user_id}', '{deadline.title}', " \
                  f"'{deadline.description}', '{deadline.date}', '{deadline.time}')"
        self.__execute_command(command)

    def update_daily_deadlines_part(self, current_date_time: DateTime):
        current_time = current_date_time.time

        self.__truncate_table('daily_deadlines_part')
        get_daily_deadlines = 'SELECT * FROM daily_deadlines'
        daily_deadlines = self.__execute_command(get_daily_deadlines)

        for deadline in daily_deadlines:
            date_time = DateTime(date=deadline[4], time=deadline[5])
            if date_time.compare_by_time(current_time):

                data = {
                    'title': deadline[2],
                    'description': deadline[3],
                    'date': deadline[4],
                    'time': deadline[5]
                }
                current_deadline = Deadline(user_id=deadline[1], data=data)

                self.__insert_daily_deadline_part(deadline[0], current_deadline)

        Logger.info('daily deadlines parts updated')

    def get_daily_deadlines_part(self, time: str):
        command = f"SELECT * FROM daily_deadlines_part WHERE time = '{time}'"
        deadlines = self.__execute_command(command)
        return deadlines

    def find_deadline(self, deadline_id: int):
        command = f'SELECT * FROM deadlines WHERE deadline_id = {deadline_id}'
        result = self.__execute_command(command)
        return result

    def is_username_saved(self, user_id: int) -> bool:
        command = f'SELECT * FROM usernames WHERE user_id={user_id}'
        result = self.__execute_command(command)
        return len(result) != 0

    def update_username(self, user_id: int, username: str):
        is_user_exists = self.is_username_saved(user_id)
        command = ' '
        if is_user_exists:
            command = f"UPDATE usernames SET username='{username}' WHERE user_id={user_id}"
        else:
            command = f"INSERT INTO usernames VALUES ({user_id}, '{username}')"

        self.__execute_command(command)

