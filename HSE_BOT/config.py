from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot_token = '5909018574:AAGY7IGcfw-QaZ_M5VPEGJ9efHPtS92RHTY'

bot = Bot(bot_token)
dispatcher = Dispatcher(bot, storage=MemoryStorage())

admin_ids = [739247496, 606667876]
