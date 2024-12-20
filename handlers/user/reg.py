from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from bot import bot
from config import config
from errors.api_error import ApiError
from gui.callbacks.UserCallback import UserCallback, UserAction
from gui.keyboards import general_keyboards
from utils import users, roles, validator, aiogram, referers


class Registration(StatesGroup):
    username = State()
    undetermined = State()
    get_referal = State()


router = Router()


async def _finish_reg(user_id: int, tag: str, state: FSMContext):
    data = await state.get_data()
    await users.create_user(**data, tag=tag)
    await state.clear()
    await bot.send_message(user_id,
                           f'Вы успешно зарегистрировались',
                           reply_markup=general_keyboards.get_menu_keyboard(roles.get_roles(user_id)))


async def try_reg(user_id: int, state: FSMContext):
    if await users.is_registered(user_id):
        raise ApiError.bad_request('Вы уже зарегистрированы')
    await bot.send_message(user_id, f"Продолжая, вы подтверждаете, что принимаете пользовательское соглашение -"
                                    f" {config.USER_AGREEMENT}")
    await bot.send_message(user_id, "Введите желаемое имя пользователя",
                           reply_markup=general_keyboards.CANCEL_MENU_KEYBOARD)
    await state.set_state(Registration.username)
    await state.update_data(user_id=user_id)


@router.message(Registration.username)
async def get_username(message: Message, state: FSMContext):
    username = message.text
    if not validator.between(len(username), config.USERNAME_MINSIZE, config.USERNAME_MAXSIZE):
        raise ApiError.validation_error(
            f"Допустимая длина ника от {config.USERNAME_MINSIZE} до {config.USERNAME_MAXSIZE} символов")
    if await users.is_username_taken(username):
        raise ApiError.bad_request("Имя пользователя уже занято")
    await state.update_data(username=message.text)
    await message.reply("У вас есть реферальный код?", reply_markup=general_keyboards.HAS_REFERAL_INKEYBOARD)
    await state.set_state(Registration.undetermined)


@router.callback_query(UserCallback.filter(F.foo == UserAction.HAS_REFERAL), Registration.undetermined)
async def has_referal(callback: CallbackQuery, state: FSMContext):
    await bot.send_message(callback.from_user.id, "Введите реферальный код")
    await state.set_state(Registration.get_referal)
    await callback.answer()


@router.message(Registration.get_referal)
async def get_referal(message: Message, state: FSMContext):
    code = aiogram.get_args(message, 1)[0]
    referer = await referers.get_referer_by_id(code)
    await state.update_data(referer_id=referer.get_id())
    await _finish_reg(message.from_user.id, message.from_user.username, state)


@router.callback_query(UserCallback.filter(F.foo == UserAction.NO_REFERAL), Registration.undetermined)
async def no_referal(callback: CallbackQuery, state: FSMContext):
    await _finish_reg(callback.from_user.id, callback.from_user.username, state)
    await callback.answer()


@router.message(Command("reg"))
async def cmd_reg(message: Message, state: FSMContext):
    await try_reg(message.from_user.id, state)
