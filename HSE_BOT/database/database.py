import sqlite3

class Database:
    connection_string = ''

    def __init__(self):
        connection = sqlite3.connect('HSE_bot.db')
        cursor = connection.cursor()
        connection.close()
        print('connected')

    def connect(self):
        pass

    def add_deadline(self):
        pass
