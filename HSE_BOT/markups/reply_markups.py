from aiogram import types
from typing import List


class ReplyMarkups:
    all_commands = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)

    def __init__(self, commands_names: List[str]):
        self.__commands_names = commands_names
        self.__init_all_commands()
        self.__init_cancel()

    def __init_all_commands(self):
        for name in self.__commands_names:
            button = types.KeyboardButton(text=name)
            self.all_commands.add(button)

    def __init_cancel(self):
        button = types.KeyboardButton('cancel')
        self.cancel.add(button)
