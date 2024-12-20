from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from utils import aiogram
from utils import validator
from utils.blacklist import blacklist

router = Router()


@router.message(Command("ban"))
async def cmd_admin_ban_user(message: Message):
    args = aiogram.get_args(message, 2)
    user_id = validator.get_int(args[1])
    blacklist.add(user_id)
    await message.reply("Пользователь заблокирован")


@router.message(Command("unban"))
async def cmd_admin_ban_user(message: Message):
    args = aiogram.get_args(message, 2)
    user_id = validator.get_int(args[1])
    blacklist.remove(user_id)
    await message.reply("Пользователь разблокирован")
