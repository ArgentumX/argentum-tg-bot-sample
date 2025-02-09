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
    keyboard = general_keyboards.get_menu_keyboard(message.from_user.id)
    await bot.send_message(message.from_user.id, text, reply_markup=keyboard)
