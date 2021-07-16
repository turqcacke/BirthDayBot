from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup
from aiogram.utils.exceptions import MessageCantBeEdited, TelegramAPIError, MessageCantBeDeleted

from data.static import INFO
from keyboards.inline import inline_options
from main import BOT
from typing import Union
from models import Information
from state.general import StateDataNames


async def edit_or_resend(text: str,
                         chat_id: int,
                         message_id: int,
                         resend: bool = False,
                         reply_markup: Union[ReplyKeyboardMarkup,
                                             ReplyKeyboardRemove,
                                             InlineKeyboardMarkup, None] = None):
    try:
        if resend:
            raise MessageCantBeEdited('Forced error')
        await BOT.edit_message_text(text=text,
                                    chat_id=chat_id,
                                    message_id=message_id,
                                    reply_markup=reply_markup)
    except (MessageCantBeEdited, TelegramAPIError):
        try:
            await BOT.delete_message(chat_id=chat_id,
                                     message_id=message_id)
        except MessageCantBeDeleted:
            pass
        await BOT.send_message(text=text,
                               chat_id=chat_id,
                               reply_markup=reply_markup)


async def edit_bind_message(result: Information,
                            chat_id: int,
                            state_data: dict,
                            resend: bool = False):
    await edit_or_resend(
        text=INFO.format(id=result.id,
                         name=result.name,
                         surname=result.surname,
                         birthday=result.day.strftime('%d.%m.%Y')),
        message_id=state_data[StateDataNames.BIND],
        chat_id=chat_id,
        reply_markup=inline_options(db_info_id=state_data[StateDataNames.INFO_ID],
                                    last_start_id=state_data[StateDataNames.LAST_START_ID]),
        resend=resend
    )
