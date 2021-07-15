from aiogram.dispatcher import Dispatcher
from .menu import pagination_handler
from aiogram.dispatcher.filters import Text
from keyboards.callbakcs import pagination_callback


async def general(callback, state):
    await callback.answer(str(callback.data))


def setup_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(pagination_handler,
                                       Text(contains=pagination_callback.prefix),
                                       state='*')
    dp.register_callback_query_handler(general,
                                       state='*')
