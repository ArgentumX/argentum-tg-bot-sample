from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import config
from enums.role import Role
from gui.callbacks.user_callback import UserCallback, UserAction

ADMIN_MENU_KEYBOARD = ReplyKeyboardMarkup(keyboard=[[
]], resize_keyboard=True)

DEFAULT_MENU_KEYBOARD = ReplyKeyboardMarkup(keyboard=[[
]], resize_keyboard=True)

CANCEL_MENU_KEYBOARD = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text=config.CANCEL_STATE)
]], resize_keyboard=True)

HAS_REFERAL_INKEYBOARD = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Да", callback_data=UserCallback(foo=UserAction.HAS_REFERAL).pack()),
    InlineKeyboardButton(text="Нет", callback_data=UserCallback(foo=UserAction.NO_REFERAL).pack())
]])


def get_pay_inkeyboard(pay_link: str):
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Оплатить", url=pay_link)
    ]])


def get_menu_keyboard(roles: list[Role]) -> ReplyKeyboardMarkup:
    res = None
    if Role.ADMIN in roles:
        res = ADMIN_MENU_KEYBOARD
    else:
        res = DEFAULT_MENU_KEYBOARD
    return res
