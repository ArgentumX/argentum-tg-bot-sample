from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot import bot
from config import config
from gui.keyboards import general_keyboards
from gui.messages import general_messages
from utils import users, aiogram, validator

router = Router()

@router.message(Command("profile"))
async def cmd_help(message: Message):
    user_id = message.from_user.id
    user = await users.get_user_by_id(user_id)
    referer = await user.get_referer()
    await bot.send_message(message.from_user.id, general_messages.get_user_info(user, referer))
