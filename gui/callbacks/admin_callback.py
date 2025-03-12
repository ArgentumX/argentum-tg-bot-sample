from aiogram.filters.callback_data import CallbackData

from gui.callbacks.base_action import BaseAction


class AdminAction(BaseAction):
    CONFIRM_NOTIFY = "CONFIRM_NOTIFY"


ADMIN_PREFIX = "admin"


class AdminCallback(CallbackData, prefix=ADMIN_PREFIX):
    foo: AdminAction
    value: int = -1
