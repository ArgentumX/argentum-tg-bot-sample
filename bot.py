from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import config

bot = Bot(token=config.TELEGRAM_TOKEN)
storage = MemoryStorage()
dp: Dispatcher = Dispatcher(storage=storage)

__all__ = ['dp', 'bot', "storage"]
