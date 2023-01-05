from aiogram.utils import executor
from config import dispatcher
import filters, handlers

if __name__ == '__main__':
    print('Trying to start bot')
    try:
        executor.start_polling(dispatcher)
    except:
        print('Error with starting bot')
