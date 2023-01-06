from aiogram.utils import executor
from config import dispatcher
import filters, handlers, errors


@dispatcher.message_handler(commands=['start'])
async def echo(message):
    await message.answer('ddd')

if __name__ == '__main__':
    print('Start bot')
    try:
        executor.start_polling(dispatcher)
    except:
        print('Error with starting bot')
