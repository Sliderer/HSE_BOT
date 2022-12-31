from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from config import dispatcher
from states import Parsing


@dispatcher.message_handler(commands='parse_ruz')
async def start_parsing_ruz(message: types.Message):
    await message.answer('Введите ваше ФИО')
    await Parsing.writing_user_name.set()


@dispatcher.message_handler(state=Parsing.writing_user_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await message.answer(f'This is your schedule {message.text}')
    await state.reset_state()
