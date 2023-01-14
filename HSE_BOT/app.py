from aiogram.utils import executor
from config import dispatcher, date_time_parser, database
import filters, handlers, errors
from multiprocessing import Process
import schedule


def start_bot():
    print('Trying to start bot')
    try:
        executor.start_polling(dispatcher)
    except:
        print('BOT NOT STARTED')
        return


def start_schedule():
    schedule.every().minute.do(date_time_parser.parse_date_time)

    schedule.every().day.at('16:08').do(lambda: (
        database.update_daily_deadlines(date_time_parser.current_date_time)
    ))

    # schedule.every(6).hours.do(lambda: (
    #    database.update_daily_deadlines_part(date_time_parser.current_date_time_update)
    # ))

    schedule.every().day.at('16:08').do(lambda: (
       database.update_daily_deadlines_part(date_time_parser.current_date_time_update)
    ))


    print('Run scheduling')
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    bot_thread = Process(target=start_bot)
    schedule_thread = Process(target=start_schedule)

    bot_thread.start()
    schedule_thread.start()

    bot_thread.join()
    schedule_thread.join()
