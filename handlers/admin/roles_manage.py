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
async def set_rang_cmd(message: Message):
    args = aiogram.get_args(message, 3)
    user_id = validator.get_int(args[1])
    role_id = args[2].upper()
    role = Role.get_by_name(role_id)
    roles.add_role(user_id, role)
    await message.reply("Успешно")


@router.message(Command('remove_role'))
async def set_rang_cmd(message: Message):
    args = aiogram.get_args(message, 3)
    user_id = validator.get_int(args[1])
    role_id = args[2].upper()
    role = Role.get_by_name(role_id)
    roles.remove_role(user_id, role)
    await message.reply("Успешно")


@router.message(Command('role_users'))
async def set_rang_cmd(message: Message):
    args = aiogram.get_args(message, 2)
    role_id = args[1].upper()
    role = Role.get_by_name(role_id)
    role_users = roles.get_users(role)
    await message.reply(f"{role_id}: {role_users}")
