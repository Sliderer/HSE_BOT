from aiogram.dispatcher.filters.state import State, StatesGroup


class CreatingDeadline(StatesGroup):
    Title = State()
    Description = State()
    Date = State()