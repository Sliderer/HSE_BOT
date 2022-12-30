from config import dispatcher, bot
from aiogram import types


@dispatcher.message_handler(text='/start')
async def start_bot(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}. I am a bot for HSE students!')
