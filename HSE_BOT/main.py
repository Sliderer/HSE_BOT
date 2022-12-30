from config import bot_token
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

bot = Bot(bot_token)
dispatcher = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dispatcher)
