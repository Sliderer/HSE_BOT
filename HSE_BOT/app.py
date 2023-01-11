from aiogram.utils import executor
from config import dispatcher
import filters, handlers, errors
from multiprocessing import Process


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


import schedule


def start_bot():
    print('Trying to start bot')
    try:
        executor.start_polling(dispatcher)
    except:
        print('BOT NOT STARTED')
        return


def start_shedule():
    #schedule.every().day.at('00:00').do(database.)
    #schedule.every(6).hours().do(тянем дедлайны на 6 часов)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    bot_thread = Process(target=start_bot)
    schedule_thread = Process(target=start_shedule)

    bot_thread.start()
    schedule_thread.start()

    bot_thread.join()
    schedule_thread.join()
