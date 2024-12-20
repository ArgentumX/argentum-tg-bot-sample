from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from utils.blacklist import Blacklist


class BannedMiddleware(BaseMiddleware):
    def __init__(self, blacklist: Blacklist, *args, **kwargs):
        self.blacklist = blacklist
        super().__init__(*args, **kwargs)

    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        if not self.blacklist.contains(event.from_user.id):
            return await handler(event, data)
