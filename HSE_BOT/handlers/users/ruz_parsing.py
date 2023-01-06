from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from config import dispatcher
from states import Parsing
import threading
from ruz_parser import Parser

@dispatcher.message_handler(commands='parse_ruz')
async def start_parsing_ruz(message: types.Message):
    await message.answer('Enter your full name/help')
    await Parsing.writing_user_name.set()


@dispatcher.message_handler(state=Parsing.writing_user_name)
async def get_full_name(message: types.Message, state: FSMContext):
    name = message.text
    thread = threading.Thread(target=get_shedule, kwargs={'name': name})
    thread.start()
    await state.reset_state()

def get_shedule(name):
    parser = Parser()
    answer = parser.get_lessons(name)
    print(answer)