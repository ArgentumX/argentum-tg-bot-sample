from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove

from config import config
from enums.role import Role
from utils.roles import roles

ADMIN_MENU_KEYBOARD = ReplyKeyboardRemove()

DEFAULT_MENU_KEYBOARD = ReplyKeyboardRemove()

CANCEL_MENU_KEYBOARD = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text=config.CANCEL_STATE)
]], resize_keyboard=True)

def get_menu_keyboard(user_id: int) -> ReplyKeyboardMarkup | ReplyKeyboardRemove:
    user_roles = roles.get_roles(user_id)
    res = DEFAULT_MENU_KEYBOARD
    if Role.ADMIN in user_roles:
        res = ADMIN_MENU_KEYBOARD
    return res