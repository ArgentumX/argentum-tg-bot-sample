from bot import bot
from enums.role import Role
from utils import users
from utils.roles import roles


async def notify_admins(message: str) -> None:
    for admin_id in roles.get_users(Role.ADMIN):
        await bot.send_message(admin_id, message)


async def notify_moderators(message: str) -> None:
    for moder_id in roles.get_users(Role.MODERATOR):
        await bot.send_message(moder_id, message)

async def notify_all(text: str) -> None:
    users_list = await users.get_all_users()
    for user in users_list:
        await bot.send_message(user.get_id(), text)