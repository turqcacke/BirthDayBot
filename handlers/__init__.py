from .commands import setup_commands, Commands
from .callback import setup_callback_handlers
from aiogram import Dispatcher
from aiogram import types


async def default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand(str(Commands.start), 'Запустить/перезапустить'),
        types.BotCommand(str(Commands.congratulate), 'Отправить поздравления'),
        types.BotCommand(str(Commands.ls), 'Список')
    ])


def setup(dp: Dispatcher):
    setup_callback_handlers(dp)
    setup_commands(dp)
