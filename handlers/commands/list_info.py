from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from keyboards.inline import inline_persons
from data.static import MENU_MESSAGE


async def list_info(message: Message, state: FSMContext):
    await message.answer(MENU_MESSAGE, reply_markup=inline_persons())
