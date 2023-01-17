from aiogram.dispatcher.filters.state import State, StatesGroup


class CreatingDeadline(StatesGroup):
    title = State()
    description = State()
    date = State()
    time = State()