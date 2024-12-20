from aiogram import Router, F
from aiogram.types import Message

from bot import bot
from gui.keyboards import general_keyboards
from gui.messages import general_messages
from utils import roles

router = Router()


@router.message(F.text)
async def unexpected_message_handler(message: Message):
    text = general_messages.UNEXPECTED_ACTION_MESSAGE
    user_roles = roles.get_roles(message.from_user.id)
    keyboard = general_keyboards.get_menu_keyboard(user_roles)
    await bot.send_message(message.from_user.id, text, reply_markup=keyboard)
