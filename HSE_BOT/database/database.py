import sqlite3


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

    def add_deadline(self):
        pass

    def find_user(self) -> bool:
        command = 'SELECT * FROM users'
        result = self.__execute_command(command)
        return len(result) != 0

    def add_user(self, user_id: int, first_name: str, second_name: str):
        if not self.find_user():
            command = f"INSERT INTO users VALUES ({user_id}, '{first_name}', '{second_name}')"
            self.__execute_command(command)
