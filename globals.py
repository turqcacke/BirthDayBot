from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import BOT_TOKEN
from aiogram.types import ParseMode
from aiogram import Bot, Dispatcher
from aiojobs import create_scheduler


class SchedulerSpawner:
    def __init__(self):
        self.scheduler = None

    async def scheduler_run(self):
        self.scheduler = await create_scheduler()

    async def scheduler_close(self):
        if self.scheduler:
            await self.scheduler.close()

    def get(self):
        return self.scheduler

    def __bool__(self):
        return True if self.scheduler is not None else False


BOT = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
DP = Dispatcher(bot=BOT, storage=MemoryStorage())
scheduler = SchedulerSpawner()
jobs = []
