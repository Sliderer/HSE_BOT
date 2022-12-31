from config import dispatcher, bot, admin_ids
from filters import IsChatPrivate
from aiogram import types


@dispatcher.message_handler(IsChatPrivate(), user_id=admin_ids, text='secret')
async def admin_handler(message: types.Message):
    await bot.send_message(message.chat.id, message)
