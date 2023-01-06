import datetime, string

from config import dispatcher, database
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from states import CreatingDeadline
from models import Deadline


@dispatcher.message_handler(commands=['create_deadline'], state=None)
async def start_creating_deadline(message: types.Message):
    await message.answer('Enter a title')
    await CreatingDeadline.first()


@dispatcher.message_handler(state=CreatingDeadline.Title)
async def getting_title(message: types.Message, state: FSMContext):

    title = message.text
    await message.answer('Enter a description')
    await state.update_data(title=title)
    await CreatingDeadline.next()


@dispatcher.message_handler(state=CreatingDeadline.Description)
async def getting_description(message: types.Message, state: FSMContext):
    description = message.text

    await message.answer('Enter a date')

    await state.update_data(description=description)
    await CreatingDeadline.next()


@dispatcher.message_handler(state=CreatingDeadline.Date)
async def get_date(message: types.Message, state: FSMContext):
    date = message.text
    try:
        date = datetime.datetime.strptime(date, '%d.%m.%Y').date()
    except:
        try:
            date = datetime.datetime.strptime(date, '%d %m %Y').date()
        except:
            try:
                date = datetime.datetime.strptime(date, '%d:%m:%Y').date()
            except:
                await message.answer('Enter date in format d:m:y or d.m.Y')
                return

    await state.update_data(date=date)
    await CreatingDeadline.next()
    await message.answer('Enter time')


@dispatcher.message_handler(state=CreatingDeadline.Time)
async def getting_time(message: types.Message, state: FSMContext):
    time = message.text

    try:
        time = datetime.datetime.strptime(time, '%H:%M').time()
    except:
        try:
            time = datetime.datetime.strptime(time, '%H.%M').time()
        except:
            try:
                time = datetime.datetime.strptime(time, '%H %M').time()
            except:
                await message.answer('Enter time if format H:M or H.M')
                return

    await state.update_data(time=time)

    data = await state.get_data()
    user_id = message.from_user.id
    deadline = Deadline(data, user_id)

    database.add_deadline(deadline)

    await message.answer(str(deadline))
    await state.reset_state()
