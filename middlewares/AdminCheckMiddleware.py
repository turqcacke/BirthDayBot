from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import Update
from data.config import ADMINS
from main import BOT


class AdminCheck(BaseMiddleware):

    async def on_process_update(self, update: Update, data: dict):
        message = None

        if update.message:
            message = update.message
        elif update.callback_query:
            message = update.callback_query.message

        if message:
            chat_id = str(message.chat.id)
            if chat_id in ADMINS:
                return
            if message.chat.id == message.from_user.id:
                await BOT.send_message(chat_id=message.chat.id,
                                       text='Started')
        if update.callback_query:
            await update.callback_query.answer('Insufficient rights.',
                                               show_alert=True)
        raise CancelHandler
