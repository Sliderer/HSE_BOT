import asyncio

from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from config import dispatcher, bot
from states import ParsingWeekSchedule
from states import ParsingDaySchedule
import threading
from ruz_parser import Parser
from config import reply_markups
from models import ScheduleFormatter
from config import parser
import ruz


@dispatcher.message_handler(text='Week schedule')
async def start_parsing_ruz_week(message: types.Message):
    # await message.answer(ruz.person_lessons("panikulshin@edu.hse.ru"), reply_markup=reply_markups.cancel)
    await message.answer('Enter your full name', reply_markup=reply_markups.cancel)
    await ParsingWeekSchedule.writing_user_name.set()


@dispatcher.message_handler(text='Day schedule')
async def start_parsing_ruz_day(message: types.Message):
    await message.answer('Enter your full name', reply_markup=reply_markups.cancel)
    await ParsingDaySchedule.writing_user_name.set()


@dispatcher.message_handler(state=ParsingWeekSchedule.writing_user_name)
async def get_full_name(message: types.Message, state: FSMContext):
    name = message.text

    if message.text == 'cancel':
        await message.answer('Canceled', reply_markup=reply_markups.all_commands)
        await state.reset_state()
        return

    answer = parser.get_week_schedule(name)
    formatted_schedule = ScheduleFormatter.get_good_form(answer)
    await message.answer(formatted_schedule)
    # thread = threading.Thread(target=asyncio.run, args=(get_shedule(name, message),))
    # thread.start()
    await state.reset_state()


@dispatcher.message_handler(state=ParsingDaySchedule.writing_user_name)
async def get_full_name(message: types.Message, state: FSMContext):
    name = message.text

    if message.text == 'cancel':
        await message.answer('Canceled', reply_markup=reply_markups.all_commands)
        await state.reset_state()
        return

    answer = parser.get_day_schedule(name)
    formatted_schedule = ScheduleFormatter.get_good_form(answer)
    await message.answer(formatted_schedule)
    # thread = threading.Thread(target=asyncio.run, args=(get_shedule(name, message),))
    # thread.start()
    await state.reset_state()


async def get_week_schedule(name, message):
    answer = parser.get_week_schedule(name)
    await bot.send_message(message.chat.id, answer)


async def get_day_schedule(name, message):
    answer = parser.get_day_schedule(name)
    await bot.send_message(message.chat.id, answer)
