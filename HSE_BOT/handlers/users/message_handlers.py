from config import dispatcher, database, reply_markups
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from filters import IsChatPrivate
from models import User


@dispatcher.message_handler(IsChatPrivate(), commands=['start'])
async def start_bot(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    second_name = message.from_user.last_name

    user = User(user_id, first_name, second_name)
    database.add_user(user)

    await message.answer(f'Hello {message.from_user.first_name}. I am a bot for HSE students!',
                         reply_markup=reply_markups.all_commands)


@dispatcher.message_handler(text='Help')
async def help(message: types.Message):
    from config import commands_names
    await message.answer('Here are all my commands:')
    await message.answer('\n'.join(commands_names))
