from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsChatPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE
