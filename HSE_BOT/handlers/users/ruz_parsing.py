import asyncio

from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from config import dispatcher, bot
from states import Parsing
import threading
from ruz_parser import Parser
from models import ScheduleFormatter


@dispatcher.message_handler(commands='parse_ruz')
async def start_parsing_ruz(message: types.Message):
    await message.answer('Enter your full name')
    await Parsing.writing_user_name.set()


@dispatcher.message_handler(state=Parsing.writing_user_name)
async def get_full_name(message: types.Message, state: FSMContext):
    name = message.text
    parser = Parser()
    answer = parser.get_week_schedule(name)
    formatted_schedule = ScheduleFormatter.get_good_form(answer)
    await message.answer(formatted_schedule)
    # thread = threading.Thread(target=asyncio.run, args=(get_shedule(name, message),))
    # thread.start()
    await state.reset_state()


async def get_week_schedule(name, message):
    parser = Parser()
    answer = parser.get_week_schedule(name)
    await bot.send_message(message.chat.id, answer)

async def get_day_schedule(name, message):
    parser = Parser()
    answer = parser.get_day_schedule(name)
    await bot.send_message(message.chat.id, answer)