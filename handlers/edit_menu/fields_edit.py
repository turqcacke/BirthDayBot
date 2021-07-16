from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from state.general import StateDataNames
from models import Session, Information
from ..utils.messages import edit_bind_message


async def data_session_statedata(state: FSMContext):
    session = Session()
    state_data = await state.get_data()
    result: Information = session.query(Information)\
        .where(Information.id == state_data[StateDataNames.INFO_ID]).one_or_none()
    return result, session, state_data


async def finish_session(state: FSMContext,
                         session: Session):
    await state.reset_state(with_data=False)

    session.commit()
    session.close()


async def edit_name(message: Message, state: FSMContext):
    result, session, state_data = await data_session_statedata(state)

    result.name = message.text
    session.flush()

    await edit_bind_message(result,
                            message.chat.id,
                            state_data,
                            resend=True)

    await finish_session(state, session)


async def edit_surname(message: Message, state: FSMContext):
    result, session, state_data = await data_session_statedata(state)

    result.surname = message.text
    session.flush()

    await edit_bind_message(result,
                            message.chat.id,
                            state_data)

    await finish_session(state, session)


async def edit_birthday(message: Message, state: FSMContext):
    from datetime import datetime

    result, session, state_data = await data_session_statedata(state)

    try:
        result.day = datetime.strptime(message.text, '%d.%m.%Y').date()
    except ValueError:
        await message.answer('Please enter correct date.')
        session.close()
    session.flush()

    await edit_bind_message(result,
                            message.chat.id,
                            state_data)

    await finish_session(state, session)
