from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.callbakcs import pagination_callback
from keyboards.inline import inline_persons
from data.static import PAGINATION


async def pagination_handler(callback: CallbackQuery, state: FSMContext):
    data = pagination_callback.parse(callback.data)
    start_id = int(data['start_id'])
    await callback.message.edit_reply_markup(reply_markup=inline_persons(PAGINATION, start_id))
