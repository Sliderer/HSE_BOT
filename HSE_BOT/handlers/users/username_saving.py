from config import dispatcher, database
from aiogram import types
from states import SavingUsername


@dispatcher.message_handler(commands=['save_name'])
async def username_saving(message: types.Message):
    await message.answer('Please send your full name')
    await SavingUsername.first()


@dispatcher.message_handler(state=SavingUsername.entering_name)
async def get_username(message: types.Message):
    username = message.text
    user_id = message.from_user.id
    #checking if student existing
    database.update_username(user_id, username)
    await message.answer('Saved!')


