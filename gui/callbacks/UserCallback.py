from aiogram.filters.callback_data import CallbackData

from gui.callbacks.BaseAction import BaseAction


class UserAction(BaseAction):
    HAS_REFERAL = "HAS_REFERAL"
    NO_REFERAL = "NO_REFERAL"


USER_PREFIX = "default"


class UserCallback(CallbackData, prefix=USER_PREFIX):
    foo: UserAction
    value: int = -1
