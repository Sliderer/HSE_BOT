import sqlite3
from models import Deadline, User


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

        command = f"INSERT INTO deadlines VALUES ({user_id}, '{title}', '{description}', '{date}', '{time}')"
        self.__execute_command(command)

    def is_user_exists(self, user: User) -> bool:
        command = f'SELECT * FROM users WHERE user_id={user.user_id}'
        result = self.__execute_command(command)
        return len(result) != 0

    def find_user(self, user: User) -> list[User]:
        command = f'SELECT * FROM users WHERE user_id={user.user_id}'
        result = self.__execute_command(command)
        return result

    def add_user(self, user: User):
        if not self.is_user_exists(user):
            command = f"INSERT INTO users VALUES ({user.user_id}, '{user.first_name}', '{user.second_name}')"
            self.__execute_command(command)
