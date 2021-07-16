from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import BOT_TOKEN
from aiogram.types import ParseMode


BOT = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
DP = Dispatcher(bot=BOT, storage=MemoryStorage())


async def on_start_polling(dp: Dispatcher):
    from middlewares import setup as middleware_setup
    from handlers import default_commands, \
        setup as setup_handlers

    middleware_setup(dp)
    await default_commands(dp)
    setup_handlers(dp)


async def on_shutdown_polling(dp: Dispatcher):
    dp.stop_polling()


if __name__ == '__main__':
    executor.start_polling(dispatcher=DP,
                           on_startup=on_start_polling,
                           on_shutdown=on_shutdown_polling,
                           skip_updates=True)
