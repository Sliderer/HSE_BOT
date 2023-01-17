from aiogram.dispatcher.filters.state import StatesGroup, State


class SavingUsername(StatesGroup):
    entering_name = State()
