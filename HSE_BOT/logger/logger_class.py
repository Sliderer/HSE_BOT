import enum
from enum import Enum


class LogTypeEnum(enum.Enum):
    INFO = 'INFO'
    WARNING = 'WARNING'
    FATAL = 'FATAL'


class Logger:
    @staticmethod
    def __send_log(log_type: LogTypeEnum, text: str):
        text = text.upper()

        print(f'{log_type.value}: {text}')
        print('-' * 50)

    @staticmethod
    def info(text: str):
        Logger.__send_log(LogTypeEnum.INFO, text)

    @staticmethod
    def warning(text: str):
        Logger.__send_log(LogTypeEnum.WARNING, text)

    @staticmethod
    def fatal(text: str):
        Logger.__send_log(LogTypeEnum.FATAL, text)
