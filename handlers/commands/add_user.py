from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from models import Session, Information
from datetime import datetime


async def invalid_input(message: Message, state: FSMContext):
    await message.answer('Invalid input.\nExample: <i>/add name:surname:01.02.1800</i>')


async def add_info(message: Message, state: FSMContext):
    command = '/add '
    text = message.text.replace(command, '')

    name, surname, day = text.split(':')

    try:
        day = datetime.strptime(day, '%d.%m.%Y').date()
    except ValueError:
        await message.answer('Please enter correct date.')
        return

    session = Session()
    new_info = Information(name=name,
                           surname=surname,
                           day=day)
    session.flush()
    session.add(new_info)
    session.commit()

    await message.answer(f'User added with id {new_info.id}.')
