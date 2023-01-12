from config import dispatcher, bot, admin_ids, date_time_parser
from filters import IsChatPrivate
from aiogram import types
from date_time_parsing import DateTime


@dispatcher.message_handler(IsChatPrivate(), user_id=admin_ids, commands=['message_info'])
async def admin_handler(message: types.Message):
    await bot.send_message(message.chat.id, message)


@dispatcher.message_handler(IsChatPrivate(), user_id=admin_ids, commands=['parse_time'])
async def time_parsing(message: types.Message):
    pass
    #print('dd' + str(date_time_parser.date_time))
    #await message.answer(str(date_time_parser.date_time))
