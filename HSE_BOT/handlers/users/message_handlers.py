from config import dispatcher, database
from aiogram import types
from filters import IsChatPrivate
from models import User


@dispatcher.message_handler(IsChatPrivate(), commands='start')
async def start_bot(message: types.Message):
    await message.answer(f'Hello {message.from_user.first_name}. I am a bot for HSE students!')
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    second_name = message.from_user.last_name

    user = User(user_id, first_name, second_name)
    database.add_user(user)


@dispatcher.message_handler(commands=['help'])
async def help(message: types.Message):
    from config import commands_names
    await message.answer('Here are all my commands:')
    await message.answer('\n'.join(commands_names))
