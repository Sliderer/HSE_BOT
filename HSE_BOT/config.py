from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import Database
from date_time_parsing import DateTimeParser
from markups import ReplyMarkups

bot_token = '5909018574:AAGY7IGcfw-QaZ_M5VPEGJ9efHPtS92RHTY'
second_bot_token = '5622163441:AAH76Zrx5YBSAuQ3RxdfPiVVeaITWxMJ8DI'

bot = Bot(bot_token)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

admin_ids = [739247496, 606667876]

commands_names = ['Parse my week schedule', 'Create a deadline', 'Help', 'Parse current time', 'Save my name']

database = Database()

reply_markups = ReplyMarkups(commands_names)

date_time_parser = DateTimeParser()

