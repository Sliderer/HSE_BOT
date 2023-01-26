from aiogram.utils import executor
from config import dispatcher, date_time_parser, database, bot, parser
import filters, handlers, errors
from multiprocessing import Process
import schedule, asyncio
from logger import Logger


def start_bot():
    Logger.info('Start bot')
    try:
        executor.start_polling(dispatcher)
    except:
        Logger.fatal('Bot not started')
        return


async def check_current_deadlines():
    Logger.info('Checking runtime deadlines')
    date_time_parser.parse_date_time()
    current_time = date_time_parser.current_date_time.time
    current_time += ':00'
    deadlines = database.get_daily_deadlines_part(current_time)

    for deadline in deadlines:
        await bot.send_message(deadline[1], deadline[2])


def start_schedule():
    schedule.every().minute.do(lambda: (
        asyncio.get_event_loop().run_until_complete(check_current_deadlines())
    ))

    schedule.every().day.at('14:49').do(lambda: (
        database.update_daily_deadlines(date_time_parser.current_date_time)
    ))

    schedule.every().day.at('14:49').do(lambda: (
        database.update_daily_deadlines_part(date_time_parser.current_date_time_update)
    ))

    Logger.info('run scheduling')
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    Logger.info('start processes')
    bot_thread = Process(target=start_bot)
    schedule_thread = Process(target=start_schedule)

    bot_thread.start()
    schedule_thread.start()

    bot_thread.join()
    schedule_thread.join()
