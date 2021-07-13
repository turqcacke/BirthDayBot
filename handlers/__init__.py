from .commands import setup_commands, Commands
from aiogram import Dispatcher
from aiogram import types


async def default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand(str(Commands.start), 'Запустить/перезапустить'),
        types.BotCommand(str(Commands.congratulate), 'Отправить поздравления')
    ])


def setup(dp: Dispatcher):
    setup_commands(dp)
