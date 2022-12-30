from aiogram.utils import executor
from config import dispatcher
import handlers

if __name__ == '__main__':
    try:
        executor.start_polling(dispatcher)
    except:
        print('Error with starting bot')
