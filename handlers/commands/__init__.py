from enum import Enum
from .congratulate import congratulate
from aiogram import Dispatcher
from aiogram.types import ContentTypes


class Commands(Enum):
    start = 'start'
    congratulate = 'congratulate'

    def __str__(self):
        return '/' + self.value


def setup_commands(dp: Dispatcher):
    dp.register_message_handler(congratulate,
                                commands=[Commands.congratulate.value, ],
                                content_types=ContentTypes.TEXT,
                                state='*')
