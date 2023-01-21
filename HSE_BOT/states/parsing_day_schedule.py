from aiogram.dispatcher.filters.state import StatesGroup, State


class ParsingDaySchedule(StatesGroup):
    writing_user_name = State()
