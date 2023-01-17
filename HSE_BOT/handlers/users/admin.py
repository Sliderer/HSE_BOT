from config import dispatcher, bot, admin_ids, date_time_parser, reply_markups
from filters import IsChatPrivate
from aiogram import types
from date_time_parsing import DateTime


@dispatcher.message_handler(IsChatPrivate(), user_id=admin_ids, commands=['message_info'])
async def admin_handler(message: types.Message):
    await bot.send_message(message.chat.id, message, reply_markup=reply_markups.all_commands)


@dispatcher.message_handler(IsChatPrivate(), user_id=admin_ids, commands=['parse_time'])
async def time_parsing(message: types.Message):
    pass
