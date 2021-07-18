import aiojobs
from aiogram import Dispatcher, executor
from globals import *


async def on_start_polling(dp: Dispatcher):
    from middlewares import setup as middleware_setup
    from handlers import default_commands, \
        setup as setup_handlers

    await scheduler.scheduler_run()

    middleware_setup(dp)
    await default_commands(dp)
    setup_handlers(dp)


async def on_shutdown_polling(dp: Dispatcher):
    if scheduler:
        for job in jobs:
            await job.wait(2)
        await scheduler.scheduler_close()
    dp.stop_polling()


if __name__ == '__main__':
    executor.start_polling(dispatcher=DP,
                           on_startup=on_start_polling,
                           on_shutdown=on_shutdown_polling,
                           skip_updates=True)
