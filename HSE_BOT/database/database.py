import sqlite3
from models import Deadline, User
from typing import List
from models import DateTime

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

        command = f"INSERT INTO deadlines VALUES (NULL, {user_id}, '{title}', '{description}', '{date}', '{time}')"
        self.__execute_command(command)

    def is_user_exists(self, user: User) -> bool:
        command = f'SELECT * FROM users WHERE user_id={user.user_id}'
        result = self.__execute_command(command)
        return len(result) != 0

    def find_user(self, user: User) -> List[User]:
        command = f'SELECT * FROM users WHERE user_id={user.user_id}'
        result = self.__execute_command(command)
        return result

    def add_user(self, user: User):
        if not self.is_user_exists(user):
            command = f"INSERT INTO users VALUES ({user.user_id}, '{user.first_name}', '{user.second_name}')"
            self.__execute_command(command)

    def __insert_daily_deadline(self, deadline_id: int, date: str, time: str):
        command = f"INSERT INTO daily_deadlines VALUES ({deadline_id}, '{date}', '{time}')"
        self.__execute_command(command)

    def __truncate_table(self, table_name: str):
        command = f'DELETE FROM {table_name}'
        self.__execute_command(command)

    def update_daily_deadlines(self, date_time: DateTime):
        date = date_time.date
        self.__truncate_table('daily_deadlines')
        command = f"SELECT * FROM deadlines WHERE date='{date}'"
        daily_deadlines = self.__execute_command(command)
        print(daily_deadlines)
        for deadline in daily_deadlines:
            self.__insert_daily_deadline(deadline[0], deadline[4], deadline[5])
        print('DONE')

    def update_daily_deadlines_part(self, date_time: DateTime):
        date = date_time.date
        time = date_time.time
        self.__truncate_table('daily_deadlines_part')
        get_daily_deadlines = 'SELECT * FROM daily_deadlines'
        daily_deadlines = self.__execute_command(get_daily_deadlines)



        for deadline in daily_deadlines:
            pass
