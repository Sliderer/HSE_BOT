import logging
from config import dispatcher
from aiogram.types import Update

from aiogram.utils.exceptions import MessageTextIsEmpty


@dispatcher.errors_handler()
async def errors_handler(update, exception):
    if isinstance(exception, MessageTextIsEmpty):
        #logging.('Message text is empty')
        return True
