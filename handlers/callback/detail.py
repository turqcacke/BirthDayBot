from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline import detail_user_callback, inline_options
from models.db_models import Session, Information
from data.static import INFO
from ..utils.messages import edit_or_resend


async def detail(callback: CallbackQuery, state: FSMContext):
    data = detail_user_callback.parse(callback.data)
    db_info_id = data['db_info_id']
    last_start_id = data['last_start_id']

    session = Session()
    result: Information = session.query(Information).where(Information.id == db_info_id).one_or_none()
    text = INFO.format(id=result.id, name=result.name, surname=result.surname, birthday=result.day.strftime('%d.%m.%Y'))
    await edit_or_resend(message_id=callback.message.message_id,
                         chat_id=callback.message.chat.id,
                         text=text,
                         reply_markup=inline_options(db_info_id=db_info_id,
                                                     last_start_id=last_start_id))
