from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import Update
from data.config import ADMINS
from main import BOT


class AdminCheck(BaseMiddleware):

    async def on_process_update(self, update: Update, data: dict):
        if update.message:
            chat_id = str(update.message.from_user.id)
            if chat_id in ADMINS:
                return
            await BOT.forward_message(chat_id=chat_id,
                                      from_chat_id=chat_id,
                                      message_id=update.message.message_id)
        raise CancelHandler
