from bot import bot
from config import config


async def notify_admins(message: str) -> None:
    for admin_id in config.ADMINS.keys():
        flags = config.ADMINS[admin_id]
        if flags['notice']:
            await bot.send_message(admin_id, message)


async def notify_moderators(message: str) -> None:
    for admin_id in config.ADMINS.keys():
        flags = config.ADMINS[admin_id]
        if flags['moderator']:
            await bot.send_message(admin_id, message)
