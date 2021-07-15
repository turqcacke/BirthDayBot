from enum import Enum
from .congratulate import congratulate
from .list_info import list_info
from aiogram import Dispatcher
from aiogram.types import ContentTypes


class Commands(Enum):
    start = 'start'
    congratulate = 'congratulate'
    ls = 'list'

    def __str__(self):
        return '/' + self.value


def setup_commands(dp: Dispatcher):
    dp.register_message_handler(list_info,
                                commands=[Commands.ls.value],
                                content_types=ContentTypes.TEXT,
                                state='*')
    dp.register_message_handler(congratulate,
                                commands=[Commands.congratulate.value, ],
                                content_types=ContentTypes.TEXT,
                                state='*')
