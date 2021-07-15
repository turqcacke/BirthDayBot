from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from models.db_models import Session, Information
from sqlalchemy import extract
from datetime import datetime
from data.config import TIME_ZONE, CHANNEL, IMAGE_PATH
from data.static import CONGRAT_MESSAGE
from aiogram.utils.exceptions import TelegramAPIError
from main import BOT
import pytz


async def congratulate(message: Message, state: FSMContext):
    session = Session()
    date_now = datetime.now(tz=pytz.timezone(TIME_ZONE)).date()

    result = session.query(Information).where(
        extract('day', Information.day) == date_now.day
    ).where(
        extract('month', Information.day) == date_now.month
    ).all()

    congrat = False

    for person in result:
        person: Information

        if person.last_congrat is None or person.last_congrat < date_now:
            await message.answer('Someone have birthday today. Congratulating.')
            try:
                await BOT.send_photo(chat_id=CHANNEL,
                                     photo=open(IMAGE_PATH, 'rb'),
                                     caption=CONGRAT_MESSAGE.format(name=person.get_full_name()))
                person.last_congrat = date_now
                congrat = True
            except TelegramAPIError as e:
                print(str(e))
                await message.answer('Please add bot to group which is specified in the config.')

    if not result or not congrat:
        await message.answer('There is no person to congratulate today.')

    session.commit()
    session.close()
