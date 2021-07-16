from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def cancel_command(message: Message, state: FSMContext):
    await state.reset_state(with_data=False)
    await message.answer('Action canceled.')
