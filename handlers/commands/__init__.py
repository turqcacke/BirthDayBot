from enum import Enum
from aiogram import Dispatcher
from aiogram.types import ContentTypes
from .congratulate import congratulate
from .list_info import list_info
from .cancel import cancel_command
from .add_user import add_info, invalid_input


class Commands(Enum):
    start = 'start'
    congratulate = 'congratulate'
    ls = 'list'
    cancel = 'cancel'
    add = 'add'

    def __str__(self):
        return '/' + self.value


def setup_commands(dp: Dispatcher):
    dp.register_message_handler(list_info,
                                commands=[Commands.ls.value],
                                content_types=ContentTypes.TEXT,
                                state=None)
    dp.register_message_handler(congratulate,
                                commands=[Commands.congratulate.value, ],
                                content_types=ContentTypes.TEXT,
                                state='*')

    dp.register_message_handler(add_info,
                                commands=[Commands.add.value],
                                regexp='^.+:.+:[0-9]{1,2}[.][0-9]{1,2}[.][0-9]{4}$',
                                content_types=ContentTypes.TEXT,
                                state=None)
    dp.register_message_handler(invalid_input,
                                commands=[Commands.add.value],
                                state=None)

    dp.register_message_handler(cancel_command,
                                commands=[Commands.cancel.value],
                                content_types=ContentTypes.TEXT,
                                state='*')
