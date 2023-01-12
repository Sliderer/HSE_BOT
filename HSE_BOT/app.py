from aiogram.utils import executor
from config import dispatcher, date_time_parser, database
import filters, handlers, errors
from multiprocessing import Process
import schedule, time


def start_bot():
    print('Trying to start bot')
    try:
        executor.start_polling(dispatcher)
    except:
        print('BOT NOT STARTED')
        return


def start_schedule():
    schedule.every().day.at('00:00').do(lambda: (
        database.update_daily_deadlines(str(date_time_parser.date_time).split()[0])
    ))
    # schedule.every(6).hours().do(тянем дедлайны на 6 часов)
    print('Run scheduling')
    while True:
        schedule.run_pending()
        date_time_parser.parse_date_time()
        print(date_time_parser.date_time)
        time.sleep(60)


if __name__ == '__main__':
    bot_thread = Process(target=start_bot)
    schedule_thread = Process(target=start_schedule)

    bot_thread.start()
    schedule_thread.start()

    bot_thread.join()
    schedule_thread.join()
