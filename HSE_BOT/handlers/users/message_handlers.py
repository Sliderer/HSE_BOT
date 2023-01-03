from config import dispatcher
from aiogram import types
from filters import IsChatPrivate


@dispatcher.message_handler(IsChatPrivate(), commands='start')
async def start_bot(message: types.Message):
    await message.answer(f'Hello {message.from_user.id}. I am a bot for HSE students!')

@dispatcher.message_handler(commands=['help'])
async def help(message: types.Message):
    from config import commands_names
    await message.answer('Here are all my commands:')
    await message.answer('\n'.join(commands_names))