from config import dispatcher
from time_parser import TimeParser
from aiogram import types


@dispatcher.message_handler(commands=['parse_time'])
async def time_parsing(message: types.Message):
    parser = TimeParser()
    time = await parser.parse_time()
    print(time)
