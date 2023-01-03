from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from config import dispatcher
from states import Parsing
from ruz_parser import Parser

@dispatcher.message_handler(commands='parse_ruz')
async def start_parsing_ruz(message: types.Message):
    await message.answer('Enter your full name')
    await Parsing.writing_user_name.set()


@dispatcher.message_handler(state=Parsing.writing_user_name)
async def get_full_name(message: types.Message, state: FSMContext):
    parser = Parser()
    answer = await parser.parse()
    await message.answer(answer)
    await state.reset_state()
