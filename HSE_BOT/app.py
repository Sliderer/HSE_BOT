from aiogram.utils import executor
from config import dispatcher
import filters, handlers, errors
from multiprocessing import Process
import asyncio


def start_bot():
    print('start bot')
    executor.start_polling(dispatcher)


def start_schedule():
    print('schedule')
    while True:
        pass


if __name__ == '__main__':
    schedule_thread = Process(target=start_schedule)
    bot_thread = Process(target=start_bot)

    schedule_thread.start()
    bot_thread.start()

    schedule_thread.join()
    bot_thread.join()



