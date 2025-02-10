import asyncio

from aiogram import Dispatcher
from aiogram.types import BotCommand
from loguru import logger

from db import db
from handlers import router as kernel_router
# Post - initialization
from utils import listener  # noqa
from utils import notifier


async def on_startup():
    await notifier.notify_admins("Server started")


async def on_shutdown():
    await notifier.notify_admins("Server stopped")


async def register_routers(dispatcher: Dispatcher):
    dispatcher.include_router(kernel_router)

async def setup_commands():
    commands = [
        BotCommand(command="start", description="все команды"),
    ]
    await bot.set_my_commands(commands)

async def setup_all(dispatcher: Dispatcher):
    db.setup(dispatcher)
    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)
    await setup_commands()


from bot import bot, dp


async def main():
    await register_routers(dp)
    await setup_all(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logger.info("Starting bot")
        asyncio.run(main())
    except Exception as ex:
        logger.error(f"Bot stopped: {ex}")
