from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.enums.referer_rang import RefererRang
from enums.role import Role
from errors.api_error import ApiError
from utils import aiogram, validator, users
from utils.roles import roles

router = Router()


@router.message(Command('add_role'))
async def cmd_add_role(message: Message):
    args = aiogram.get_args(message, 2)
    user_id = validator.get_int(args[0])
    role_id = args[1].upper()
    role = Role.get_by_name(role_id)
    roles.add_role(user_id, role)
    await message.reply("Успешно")


@router.message(Command('remove_role'))
async def cmd_remove_role(message: Message):
    args = aiogram.get_args(message, 2)
    user_id = validator.get_int(args[0])
    role_id = args[1].upper()
    role = Role.get_by_name(role_id)
    roles.remove_role(user_id, role)
    await message.reply("Успешно")


@router.message(Command('role_users'))
async def cmd_role_users(message: Message):
    args = aiogram.get_args(message, 1)
    role_id = args[0].upper()
    role = Role.get_by_name(role_id)
    role_users = roles.get_users(role)
    await message.reply(f"{role_id}: {role_users}")
