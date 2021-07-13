from aiogram import Dispatcher, Bot, executor
from data.config import BOT_TOKEN

BOT = Bot(token=BOT_TOKEN)
DP = Dispatcher(bot=BOT)


def on_start_polling():
    pass


def on_shutdown_polling():
    pass


if __name__ == '__main__':
    executor.start_polling(dispatcher=DP,
                           on_startup=on_start_polling,
                           on_shutdown=on_shutdown_polling)
