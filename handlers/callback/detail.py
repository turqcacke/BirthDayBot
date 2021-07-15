from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline import detail_user_callback
from models.db_models import Session, Information
from data.static import INFO


async def detail(callback: CallbackQuery, state: FSMContext):
    data = detail_user_callback.parse(callback.data)
    db_info_id = data['db_info_id']
    last_start_id = data['last_start_id']

    session = Session()
    result: Information = session.query(Information).where(Information.id == db_info_id).one_or_none()
    text = INFO.format(id=result.id, name=result.name, surname=result.surname)
    await callback.message.edit_text()
#     TODO
