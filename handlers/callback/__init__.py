from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.callbacks import pagination_callback, detail_user_callback, delete_user_callback, close_callback,\
    edit_user_callback
from .detail import detail
from .menu import pagination_handler, close_handler
from .edit import delete, edit_field_handler


async def general(callback):
    await callback.answer('Finish or cancel previous action.')


def setup_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(pagination_handler,
                                       Text(contains=pagination_callback.prefix),
                                       state=None)
    dp.register_callback_query_handler(detail,
                                       Text(contains=detail_user_callback.prefix),
                                       state=None)
    dp.register_callback_query_handler(delete,
                                       Text(contains=delete_user_callback.prefix),
                                       state=None)
    dp.register_callback_query_handler(close_handler,
                                       Text(contains=close_callback.prefix),
                                       state=None)
    dp.register_callback_query_handler(edit_field_handler,
                                       Text(contains=edit_user_callback.prefix),
                                       state=None)
    dp.register_callback_query_handler(general,
                                       state='*')
