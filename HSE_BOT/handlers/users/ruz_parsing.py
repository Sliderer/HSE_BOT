import asyncio

from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from config import dispatcher, bot
from states import Parsing
import threading
from ruz_parser import Parser


@dispatcher.message_handler(commands='parse_ruz')
async def start_parsing_ruz(message: types.Message):
    await message.answer('Enter your full name')
    await Parsing.writing_user_name.set()


@dispatcher.message_handler(state=Parsing.writing_user_name)
async def get_full_name(message: types.Message, state: FSMContext):
    name = message.text
    parser = Parser()
    answer = parser.get_lessons(name)
    await message.answer(answer)
    # thread = threading.Thread(target=asyncio.run, args=(get_shedule(name, message),))
    # thread.start()
    await state.reset_state()


async def get_shedule(name, message):
    parser = Parser()
    answer = parser.get_lessons(name)
    await bot.send_message(message.chat.id, answer)
