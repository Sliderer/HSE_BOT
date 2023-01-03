from config import dispatcher
from date_time_parsing import TimeParser
from aiogram import types


@dispatcher.message_handler(commands=['parse_time'])
async def time_parsing(message: types.Message):
    parser = TimeParser()
    time = await parser.parse_time()
    await message.answer(f'The time in Moscow is: {time}')
