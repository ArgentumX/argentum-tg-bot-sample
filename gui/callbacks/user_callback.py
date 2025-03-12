from aiogram.filters.callback_data import CallbackData

from gui.callbacks.base_action import BaseAction


class UserAction(BaseAction):
    HAS_REFERAL = "HAS_REFERAL"
    NO_REFERAL = "NO_REFERAL"
    CANCEL = "CANCEL"


USER_PREFIX = "default"


class UserCallback(CallbackData, prefix=USER_PREFIX):
    foo: UserAction
    value: int = -1
