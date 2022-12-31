from config import dispatcher, bot
from aiogram import types
from filters import IsChatPrivate


@dispatcher.message_handler(IsChatPrivate(), text='/start')
async def start_bot(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello {message.from_user.id}. I am a bot for HSE students!')
