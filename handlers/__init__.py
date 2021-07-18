from .commands import setup_commands, Commands
from .callback import setup_callback_handlers
from .edit_menu import setup_edit_menu_handlers
from aiogram import Dispatcher
from aiogram import types


async def default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand(str(Commands.start), 'Запустить/перезапустить'),
        types.BotCommand(str(Commands.congratulate), 'Отправить поздравления'),
        types.BotCommand(str(Commands.ls), 'Список'),
        types.BotCommand(str(Commands.cancel), 'Отменить'),
        types.BotCommand(str(Commands.add), 'Добавить в список'),
        types.BotCommand(str(Commands.start_auto), 'Вкл. авто поздравления'),
        types.BotCommand(str(Commands.stop_auto), 'Выкл. авто поздравления')
    ])


def setup(dp: Dispatcher):
    setup_callback_handlers(dp)
    setup_commands(dp)
    setup_edit_menu_handlers(dp)
