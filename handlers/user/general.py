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


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    if not await users.is_registered(message.from_user.id):
        args = aiogram.get_args(message)
        referer_id = args[0] if len(args) > 1 else None
        user = await users.create_user(message.from_user.id, message.from_user.username, referer_id)
        await bot.send_message(message.from_user.id, general_messages.START_MESSAGE,
                               reply_markup=general_keyboards.get_menu_keyboard(message.from_user.id))
        await bot.send_message(message.from_user.id, await general_messages.get_ref_link_message(user))
        return
    await bot.send_message(message.from_user.id, general_messages.START_MESSAGE,
                           reply_markup=general_keyboards.get_menu_keyboard(message.from_user.id))