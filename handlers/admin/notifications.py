from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from bot import bot
from db.enums.referer_rang import RefererRang
from errors.api_error import ApiError
from gui.callbacks.admin_callback import AdminCallback, AdminAction
from gui.callbacks.user_callback import UserAction, UserCallback
from gui.keyboards import general_keyboards
from gui.messages import general_messages
from utils import aiogram, validator, users, notifier

router = Router()


class NotifyState(StatesGroup):
    confirm = State()



@router.message(Command('notify'))
async def set_rang_cmd(message: Message, state: FSMContext):
    text = message.text.split("/notify")[1]
    await state.set_state(NotifyState.confirm)
    await message.reply(text, reply_markup=general_keyboards.CONFIRM_NOTIFY_KB)

@router.callback_query(AdminCallback.filter(F.foo == AdminAction.CONFIRM_NOTIFY), NotifyState.confirm)
async def inline_confirm(callback: CallbackQuery, state: FSMContext):
    await notifier.notify_all(callback.message.text)
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.clear()
    await callback.answer()

@router.callback_query(UserCallback.filter(F.foo == UserAction.CANCEL), NotifyState.confirm)
async def inline_confirm(callback: CallbackQuery, state: FSMContext):
    await bot.send_message(callback.from_user.id, general_messages.CANCEL)
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.clear()
    await callback.answer()