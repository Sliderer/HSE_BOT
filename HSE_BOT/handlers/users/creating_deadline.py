import datetime
import difflib

from config import dispatcher, database, reply_markups, date_time_parser
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from states import CreatingDeadline
from models import Deadline, DateTime


async def check_answer(answer: str, state: FSMContext) -> bool:
    if answer == 'cancel':
        await state.reset_state()
        return True
    return False


@dispatcher.message_handler(commands=['create_deadline'], state=None)
async def start_creating_deadline(message: types.Message):
    await message.answer('Enter a title', reply_markup=reply_markups.cancel)
    await CreatingDeadline.first()


@dispatcher.message_handler(state=CreatingDeadline.Title)
async def getting_title(message: types.Message, state: FSMContext):
    title = message.text
    if await check_answer(message.text, state):
        await message.answer('Cancel', reply_markup=reply_markups.all_commands)
        return
    await message.answer('Enter a description', reply_markup=reply_markups.cancel)
    await state.update_data(title=title)
    await CreatingDeadline.next()


@dispatcher.message_handler(state=CreatingDeadline.Description)
async def getting_description(message: types.Message, state: FSMContext):
    description = message.text
    if await check_answer(message.text, state):
        await message.answer('Cancel', reply_markup=reply_markups.all_commands)
        return
    await message.answer('Enter a date', reply_markup=reply_markups.cancel)

    await state.update_data(description=description)
    await CreatingDeadline.next()


@dispatcher.message_handler(state=CreatingDeadline.Date)
async def get_date(message: types.Message, state: FSMContext):
    date = message.text
    if await check_answer(message.text, state):
        await message.answer('Cancel', reply_markup=reply_markups.all_commands)
        return

    try:
        date = datetime.datetime.strptime(date, '%d.%m.%Y').date()
    except:
        try:
            date = datetime.datetime.strptime(date, '%d %m %Y').date()
        except:
            try:
                date = datetime.datetime.strptime(date, '%d:%m:%Y').date()
            except:
                await message.answer('Enter date in format d:m:y or d.m.Y', reply_markup=reply_markups.cancel)
                return

    await state.update_data(date=date)
    await CreatingDeadline.next()
    await message.answer('Enter time', reply_markup=reply_markups.cancel)


@dispatcher.message_handler(state=CreatingDeadline.Time)
async def getting_time(message: types.Message, state: FSMContext):
    time = message.text
    if await check_answer(message.text, state):
        await message.answer('Cancel', reply_markup=reply_markups.all_commands)
        return

    try:
        time = datetime.datetime.strptime(time, '%H:%M').time()
    except:
        try:
            time = datetime.datetime.strptime(time, '%H.%M').time()
        except:
            try:
                time = datetime.datetime.strptime(time, '%H %M').time()
            except:
                await message.answer('Enter time if format H:M or H.M', reply_markup=reply_markups.cancel)
                return

    await state.update_data(time=time)

    data = await state.get_data()
    user_id = message.from_user.id
    deadline = Deadline(data, user_id)

    current_date_time = date_time_parser.parse_date_time() # получаем текущую дату
    last_daily_deadlines_part_update = date_time_parser.last_daily_deadlines_part_update

    deadline_id = database.add_deadline(deadline)

    print(f'DEADLINE_ID {deadline_id}')

    if current_date_time.date == deadline.date:
        database.add_deadline_to_daily_deadlines(deadline_id, deadline.date, deadline.time) #добавление в дневные дедлайны
        print('ADDED TO daily')
        deadline_date_time = DateTime(deadline.time, deadline.date)

        if deadline_date_time.compare_by_time(last_daily_deadlines_part_update.time):
            # добавляем в таблицу daily_deadline_part
            print('ADDED TO part')
            database.add_deadline_to_daily_deadlines_part(deadline_id, deadline.date, deadline.time)
    else:
        a = current_date_time.date
        b = deadline.date
        if len(a) != len(b):
            print('diff len')
        else:
            for i in range(len(a)):
                if a[i] != b[i]:
                    print(f'diff in {i}')

    await message.answer(str(deadline))
    await state.reset_state()
