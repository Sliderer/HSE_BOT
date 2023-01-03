import typing

from config import dispatcher
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from states import CreatingDeadline


@dispatcher.message_handler(commands=['create_deadline'], state=None)
async def start_creating_deadline(message: types.Message):
    await message.answer('Введите заголовок')
    await CreatingDeadline.first()


@dispatcher.message_handler(state=CreatingDeadline.Title)
async def getting_title(message: types.Message, state: FSMContext):
    await message.answer('Введите описание')
    title = message.text
    await state.update_data(title=title)
    await CreatingDeadline.next()


@dispatcher.message_handler(state=CreatingDeadline.Description)
async def getting_description(message: types.Message, state: FSMContext):
    await message.answer('Введите дату')
    description = message.text
    await state.update_data(description=description)
    await CreatingDeadline.next()


@dispatcher.message_handler(state=CreatingDeadline.Date)
async def getting_date(message: types.Message, state: FSMContext):
    date = message.text
    await state.update_data(date=date)
    data = await state.get_data()
    deadline = Deadline(data)
    await message.answer(str(deadline))
    await state.reset_state()


class Deadline:
    def __init__(self, data: typing.Dict):
        self.__title = data['title']
        self.__description = data['description']
        self.__date = data['date']

    def __str__(self):
        return f'Deadline \n' \
               f'Title: {self.__title} \n' \
               f'Description: {self.__description} \n' \
               f'Date: {self.__date}'
