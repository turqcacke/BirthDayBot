from aiogram import Dispatcher
from .AdminCheckMiddleware import AdminCheck


def setup(dp: Dispatcher):
    dp.middleware.setup(AdminCheck())
