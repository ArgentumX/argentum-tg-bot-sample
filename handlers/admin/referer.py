from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.enums.referer_rang import RefererRang
from errors.api_error import ApiError
from utils import aiogram, validator, users

router = Router()


@router.message(Command('set_rang'))
async def set_rang_cmd(message: Message):
    args = aiogram.get_args(message, 2)
    user_id = validator.get_int(args[0])
    rang_name = args[1].upper()
    if not RefererRang.has_name(rang_name):
        raise ApiError.bad_request("Неправильный ранг")
    rang = RefererRang.get_by_name(rang_name)
    referer = await (await  users.get_user_by_id(user_id)).get_referer()
    await referer.set_rang(rang)
    await message.reply("Успешно")
