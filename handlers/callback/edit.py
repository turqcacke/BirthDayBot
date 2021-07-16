from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.callbacks import delete_user_callback, edit_user_callback
from keyboards.inline import inline_persons
from models.db_models import Session, Information
from ..utils.messages import edit_or_resend
from data.static import MENU_MESSAGE
from state.general import StateDataNames, InputStates


async def delete(callback: CallbackQuery, state: FSMContext):
    data = delete_user_callback.parse(callback.data)
    db_info_id = data['db_info_id']
    last_start_id = data['last_start_id']

    session = Session()
    result = session.query(Information).where(Information.id == db_info_id).one_or_none()
    session.delete(result)
    session.commit()
    session.close()

    await edit_or_resend(message_id=callback.message.message_id,
                         chat_id=callback.message.chat.id,
                         text=MENU_MESSAGE,
                         reply_markup=inline_persons(start_index=last_start_id))
    await callback.answer('Deleted')


async def edit_field_handler(callback: CallbackQuery, state: FSMContext):
    data = edit_user_callback.parse(callback.data)
    field_name = data['field_name']
    db_info_id = data['db_info_id']
    last_start_id = data['last_start_id']

    async with state.proxy() as state_data:
        state_data[StateDataNames.BIND] = callback.message.message_id
        state_data[StateDataNames.INFO_ID] = db_info_id
        state_data[StateDataNames.LAST_START_ID] = last_start_id

    await callback.answer(f'Send {field_name}.',
                          show_alert=True)
    await getattr(InputStates, field_name).set()

