from config import dispatcher, bot, admin_ids
from filters import IsChatPrivate
from aiogram import types
from date_time_parsing import TimeParser, DateTime


@dispatcher.message_handler(IsChatPrivate(), user_id=admin_ids, text='secret')
async def admin_handler(message: types.Message):
    await bot.send_message(message.chat.id, message)


@dispatcher.message_handler(IsChatPrivate(), user_id=admin_ids, commands=['parse_time'])
async def time_parsing(message: types.Message):
    parser = TimeParser()
    date_time: DateTime = parser.parse_date_time()
    await message.answer(f'The time in Moscow is: {date_time.time}')
    await message.answer(f'The date is: {date_time.date}')
