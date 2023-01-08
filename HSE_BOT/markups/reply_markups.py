from aiogram import types
from config import commands_names


class ReplyMarkups:
    all_commands = types.ReplyKeyboardMarkup()

    def __init__(self):
        self.__init_all_commands()

    def __init_all_commands(self):
        for name in commands_names:
            button = types.KeyboardButton(text=name)
            self.all_commands.add(button)
