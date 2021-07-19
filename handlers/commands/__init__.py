from enum import Enum
from aiogram import Dispatcher
from aiogram.types import ContentTypes
from .congratulate import congratulate_by_command, congratulate_auto, stop_congratulate_auto
from .list_info import list_info
from .cancel import cancel_command
from .add_user import add_info, invalid_input


class Commands(Enum):
    start = 'start'
    congratulate = 'congratulate'
    start_auto = 'start_auto'
    stop_auto = 'stop_auto'
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
    dp.register_message_handler(congratulate_by_command,
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

    dp.register_message_handler(congratulate_auto,
                                commands=[Commands.start_auto.value],
                                state=None)

    dp.register_message_handler(stop_congratulate_auto,
                                commands=[Commands.stop_auto.value],
                                state=None)

    dp.register_message_handler(cancel_command,
                                commands=[Commands.cancel.value],
                                content_types=ContentTypes.TEXT,
                                state='*')
