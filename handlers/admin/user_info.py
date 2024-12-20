from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot import bot
from gui.messages import general_messages
from utils import aiogram, validator, users

router = Router()


@router.message(Command("user_info", "ui"))
async def cmd_admin_user_info(message: Message):
    args = aiogram.get_args(message, 2)
    user_id = validator.get_int(args[1])
    user = await users.get_user_by_id(user_id)
    text = general_messages.get_all_user_info(user)
    await bot.send_message(message.from_user.id, text)
