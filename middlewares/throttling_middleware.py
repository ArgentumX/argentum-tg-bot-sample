from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from cachetools import TTLCache

from bot import bot


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, rate_limit: int, rate_cycle: int):
        self.rate_limit = rate_limit
        self.caches = TTLCache(maxsize=10_000, ttl=rate_cycle)

    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        contains = user_id in self.caches
        requests = self.caches[user_id] if contains else [0, False]
        requests[0] += 1
        if not contains:
            self.caches[user_id] = requests
        if requests[0] > self.rate_limit:
            if not requests[1]:
                requests[1] = True
                await bot.send_message(user_id, "Вы превысили лимит запросов")
            return
        return await handler(event, data)
