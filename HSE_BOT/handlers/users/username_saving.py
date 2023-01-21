from config import dispatcher, database
from aiogram import types
from states import SavingUsername
from aiogram.dispatcher.storage import FSMContext

@dispatcher.message_handler(text='Save my name')

async def username_saving(message: types.Message):
    await message.answer('Please send your full name')
    await SavingUsername.first()


@dispatcher.message_handler(state=SavingUsername.entering_name)
async def get_username(message: types.Message, state: FSMContext):
    username = message.text
    user_id = message.from_user.id
    # checking if student existing

    if not 1:
        await message.answer('Student not found. Please enter your full name')
        return

    database.update_username(user_id, username)
    await message.answer('Saved!')
    await state.reset_state()
