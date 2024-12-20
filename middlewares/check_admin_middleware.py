from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from loguru import logger

from utils import roles


class CheckAdminMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        if not roles.is_admin(event.from_user.id):
            logger.warning(f"user {event.from_user.id} attempted to execute admin actions")
            return
        return await handler(event, data)
