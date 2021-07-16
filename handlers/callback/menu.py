from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageCantBeDeleted
from keyboards.callbacks import pagination_callback
from keyboards.inline import inline_persons
from data.static import MENU_MESSAGE
from ..utils.messages import edit_or_resend
from main import BOT


async def pagination_handler(callback: CallbackQuery, state: FSMContext):
    data = pagination_callback.parse(callback.data)
    start_id = int(data['start_id'])
    await edit_or_resend(message_id=callback.message.message_id,
                         chat_id=callback.message.chat.id,
                         text=MENU_MESSAGE,
                         reply_markup=inline_persons(start_index=start_id))


async def close_handler(callback: CallbackQuery, state: FSMContext):
    try:
        await BOT.delete_message(message_id=callback.message.message_id,
                                 chat_id=callback.message.chat.id)
    except MessageCantBeDeleted:
        await callback.answer('Something went wrong. Message can\'t be delete.But menu deprecated.')
