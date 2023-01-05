import typing
import datetime

from config import dispatcher
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from states import CreatingDeadline


@dispatcher.message_handler(commands=['create_deadline'], state=None)
async def start_creating_deadline(message: types.Message):
    await message.answer('Enter a title')
    await CreatingDeadline.first()


@dispatcher.message_handler(state=CreatingDeadline.Title)
async def getting_title(message: types.Message, state: FSMContext):
    await message.answer('Enter a description')
    title = message.text
    await state.update_data(title=title)
    await CreatingDeadline.next()


@dispatcher.message_handler(state=CreatingDeadline.Description)
async def getting_description(message: types.Message, state: FSMContext):
    await message.answer('Enter a date in format dd.mm.yyyy hh:mm')
    description = message.text
    await state.update_data(description=description)
    await CreatingDeadline.next()


@dispatcher.message_handler(state=CreatingDeadline.Date)
async def getting_date(message: types.Message, state: FSMContext):
    date, time = list(map(str, message.text.split()))
    date = datetime.datetime.strptime(date, '%d.%m.%Y').date()
    time = datetime.datetime.strptime(time, '%H:%M').time()
    await state.update_data(date=date)
    await state.update_data(time=time)
    data = await state.get_data()
    user_id = message.from_user.id
    deadline = Deadline(data, user_id)
    await message.answer(str(deadline))
    await state.reset_state()

    print()


class Deadline:
    def __init__(self, data: typing.Dict, user_id: int):
        self.__title: str = data['title']
        self.__description: str = data['description']
        self.__date = data['date']
        self.__time = data['time']
        self.__user_id = user_id

    def __str__(self):
        return f'Deadline \n' \
               f'Title: {self.__title} \n' \
               f'Description: {self.__description} \n' \
               f'Date: {self.__date} \n' \
               f'Time: {self.__time}'
