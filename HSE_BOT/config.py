from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import Database
from date_time_parsing import DateTimeParser
from markups import ReplyMarkups
from ruz_parser import Parser

bot_token = '5909018574:AAGY7IGcfw-QaZ_M5VPEGJ9efHPtS92RHTY'

bot = Bot(bot_token)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

admin_ids = [739247496, 606667876]

commands_names = ['Week schedule', 'Day schedule', 'Create a deadline', 'Help', 'Parse current time', 'Save my name']

database = Database()

date_time_parser = DateTimeParser()

parser = Parser(date_time_parser)

reply_markups = ReplyMarkups(commands_names)

