from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove

from config import config
from enums.role import Role
from gui.callbacks.admin_callback import AdminCallback, AdminAction
from gui.callbacks.user_callback import UserCallback, UserAction
from utils.roles import roles

ADMIN_MENU_KEYBOARD = ReplyKeyboardRemove()

DEFAULT_MENU_KEYBOARD = ReplyKeyboardRemove()

CANCEL_MENU_KEYBOARD = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text=config.CANCEL_STATE)
]], resize_keyboard=True)

CONFIRM_NOTIFY_KB = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подтвердить отправку", callback_data=AdminCallback(
        foo=AdminAction.CONFIRM_NOTIFY).pack())],
    [InlineKeyboardButton(text="Отмена", callback_data=UserCallback(foo=UserAction.CANCEL).pack())]
])

def get_menu_keyboard(user_id: int) -> ReplyKeyboardMarkup | ReplyKeyboardRemove:
    user_roles = roles.get_roles(user_id)
    res = DEFAULT_MENU_KEYBOARD
    if Role.ADMIN in user_roles or Role.MODERATOR in user_roles:
        res = ADMIN_MENU_KEYBOARD
    return res

