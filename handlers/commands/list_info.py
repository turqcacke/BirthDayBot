from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from keyboards.inline import inline_persons
from data.static import PAGINATION


async def list_info(message: Message, state: FSMContext):
    await message.answer('List of employee:', reply_markup=inline_persons(PAGINATION))
