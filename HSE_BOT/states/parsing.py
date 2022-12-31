from aiogram.dispatcher.filters.state import StatesGroup, State


class Parsing(StatesGroup):
    writing_user_name = State()
