from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from bot import bot
from db import db
from gui.messages import general_messages
from utils import validator, aiogram, users

router = Router()


@router.message(Command("db_recreate"))
async def cmd_admin_ban_user(message: Message):
    await db.recreate_db()
    await message.reply("Успешно")
    logger.info("db was recreated")


@router.message(Command("delete_user"))
async def cmd_admin_ban_user(message: Message):
    user_id = validator.get_int(aiogram.get_args(message, 1)[0])
    user = await users.get_user_by_id(user_id)
    await user.delete()
    logger.info(f"deleted user {user.get_id()}")

@router.message(Command("all_users"))
async def cmd_all_users(message: Message):
    all_users = await users.get_all_users()
    await bot.send_message(message.from_user.id, general_messages.get_users_list(all_users))