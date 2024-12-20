from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot import bot
from config import config
from gui.keyboards import general_keyboards
from gui.messages import general_messages
from handlers.user import reg
from utils import users

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    if not await users.is_registered(message.from_user.id):
        await reg.try_reg(message.from_user.id, state)
        return
    await bot.send_message(message.from_user.id, general_messages.START_MESSAGE,
                           reply_markup=general_keyboards.DEFAULT_MENU_KEYBOARD)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await bot.send_message(message.from_user.id, general_messages.HELP_MESSAGE,
                           reply_markup=general_keyboards.DEFAULT_MENU_KEYBOARD)


@router.message(F.text == config.USER_HELP)
async def inline_user_help(message: Message):
    await bot.send_message(message.from_user.id, general_messages.HELP_MESSAGE,
                           reply_markup=general_keyboards.DEFAULT_MENU_KEYBOARD)
