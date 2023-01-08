from aiogram import types


class ReplyMarkups:
    all_commands = types.ReplyKeyboardMarkup()

    def __init__(self, commands_names: list[str]):
        self.__commands_names = commands_names
        self.__init_all_commands()

    def __init_all_commands(self):
        for name in self.__commands_names:
            button = types.KeyboardButton(text=name)
            self.all_commands.add(button)
