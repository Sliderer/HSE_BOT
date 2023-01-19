from aiogram.dispatcher.filters.state import StatesGroup, State


class ParsingWeekSchedule(StatesGroup):
    writing_user_name = State()
