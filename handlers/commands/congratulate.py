from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from models.db_models import Session, Information
from sqlalchemy import extract
from datetime import datetime
from data.config import TIME_ZONE
import pytz


async def congratulate(message: Message, state: FSMContext):
    session = Session()
    date_now = datetime.now(tz=pytz.timezone(TIME_ZONE)).date()

    result = session.query(Information).where(
        extract('day', Information.day) == date_now.day
    ).where(
        extract('month', Information.day) == date_now.month
    ).all()

    for person in result:
        person: Information

        if person.last_congrat is None or person.last_congrat < date_now:
            # TODO: send message
            person.last_congrat = date_now

    if not result:
        await message.answer('There is no person to congratulate today.')

    session.commit()
    session.close()
