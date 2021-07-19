from aiogram.dispatcher import Dispatcher
from state.general import InputStates
from .fields_edit import edit_name, edit_birthday, edit_surname
from data.static import LENGTH_LIMIT

len_filter = lambda msg: len(msg.text) < LENGTH_LIMIT


async def name_validate(msg):
    await msg.answer(f'Invalid name. Should be length lessen {LENGTH_LIMIT}.')


async def surname_validate(msg):
    await msg.answer(f'Invalid surname. Should be length lessen {LENGTH_LIMIT}')


async def date_validate(msg):
    await msg.answer(f'Invalid date format. Should be like "01.02.1900".')


def setup_edit_menu_handlers(dp: Dispatcher):
    dp.register_message_handler(edit_name,
                                len_filter,
                                state=InputStates.name)
    dp.register_message_handler(name_validate,
                                state=InputStates.name)

    dp.register_message_handler(edit_surname,
                                len_filter,
                                state=InputStates.surname)
    dp.register_message_handler(surname_validate,
                                state=InputStates.surname)

    dp.register_message_handler(edit_birthday,
                                regexp='^[0-9]{1,2}[.][0-9]{1,2}[.][0-9]{4}$',
                                state=InputStates.day)
    dp.register_message_handler(date_validate,
                                state=InputStates.day)
