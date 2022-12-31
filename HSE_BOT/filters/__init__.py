from .private_chat_filters import IsChatPrivate
from config import dispatcher

if __name__ == '__filters__':
    dispatcher.bind_filter(IsChatPrivate)
