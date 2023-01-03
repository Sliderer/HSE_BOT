from config import dispatcher
from date_time_parsing import TimeParser
from aiogram import types


@dispatcher.message_handler(commands=['parse_time'])
async def time_parsing(message: types.Message):
    parser = TimeParser()
    date_time = parser.parse_date_time()
    await message.answer(f'The time in Moscow is: {date_time[0]}')
    await message.answer(f'The date is: {date_time[1]}')
